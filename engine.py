"""
engine.py -- the canonical 11-tick E/M/R cycle.

This exists because of a real bug found this session: every test script
before this one hand-rewrote the cycle loop, and one of them used
"revert when global_tick % 3 == 0" instead of resetting the local
position every 11 ticks. Those two rules only agree during the first
cycle -- 11 is not a multiple of 3, so a continuous global-mod-3 rule
silently drifts out of alignment with the real local E/M/R roles from
the second cycle onward. That produced a wrong result that took
several turns to catch.

This class is the fix: local position is EXPLICITLY reset to 1 at the
start of every cycle, so E/M/R role assignment can never drift, no
matter how many cycles are run. Write the cycle loop once, correctly,
here -- do not hand-roll it again elsewhere.
"""

from .erp import ERP, MEDIANT_ABSENCE
from .primality import is_prime_magnitude

ROLE_BY_LOCAL_POSITION = {
    1: 'E', 2: 'M', 3: 'R', 4: 'E', 5: 'M', 6: 'R',
    7: 'E', 8: 'M', 9: 'R', 10: 'E', 11: 'M',
}


class Tick:
    __slots__ = ('global_index', 'cycle', 'local_position', 'role', 'value', 'excluded')

    def __init__(self, global_index, cycle, local_position, role, value, excluded=None):
        self.global_index = global_index
        self.cycle = cycle
        self.local_position = local_position
        self.role = role
        self.value = value
        self.excluded = excluded  # the value excluded from propagation, if this was a Return

    def __repr__(self):
        return f"Tick(g={self.global_index}, cycle={self.cycle}, local={self.local_position}, role={self.role}, value={self.value})"


class Engine:
    """
    Runs the E/M/R cycle with correct, non-drifting local position reset.

    combine_fn: a two-argument RS operator (e.g. eta wrapped to take two
        args and ignore one, or oplus/boxplus) used at non-Return ticks.
    on_boundary: optional callback(engine, boundary_tick) fired once at
        the end of each cycle (local position 11 -> boundary), for
        wiring in Koppa/Omega deposits or other cycle-boundary logic.
    on_prime_emission: optional callback(engine, tick) fired whenever an
        Emission-role tick's numerator is prime (sign-preserving check).
    """
    def __init__(self, seed0: ERP, seed1: ERP, combine_fn, on_boundary=None, on_prime_emission=None):
        self.combine_fn = combine_fn
        self.on_boundary = on_boundary
        self.on_prime_emission = on_prime_emission
        self.history = []
        self._cycle = 0
        self._seed_prev2 = seed0
        self._seed_prev1 = seed1

    def run_cycles(self, n_cycles: int):
        global_index = 0
        for _ in range(n_cycles):
            self._cycle += 1
            cycle_values = {}
            for local_position in range(1, 12):
                global_index += 1
                role = ROLE_BY_LOCAL_POSITION[local_position]
                excluded = None

                if local_position == 1:
                    value = self.combine_fn(self._seed_prev1, self._seed_prev2)
                elif local_position == 2:
                    value = self.combine_fn(cycle_values[1], self._seed_prev1)
                elif role == 'R':
                    excluded = cycle_values[local_position - 1]  # rs-guard: allow: dict-key bookkeeping, not ERP arithmetic
                    value = cycle_values[local_position - 2]  # rs-guard: allow: dict-key bookkeeping, not ERP arithmetic
                else:
                    value = self.combine_fn(cycle_values[local_position - 1], cycle_values[local_position - 2])  # rs-guard: allow: dict-key bookkeeping, not ERP arithmetic

                cycle_values[local_position] = value
                tick = Tick(global_index, self._cycle, local_position, role, value, excluded)
                self.history.append(tick)

                if role == 'E' and self.on_prime_emission is not None:
                    if is_prime_magnitude(value.n):
                        self.on_prime_emission(self, tick)

            if self.on_boundary is not None:
                self.on_boundary(self, self.history[-1])

            # reseed next cycle from the tail of this one -- local position always
            # resets to 1 next iteration, regardless of global_index
            self._seed_prev2 = cycle_values[9]
            self._seed_prev1 = cycle_values[10]

        return self.history
