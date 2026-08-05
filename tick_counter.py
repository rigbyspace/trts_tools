"""
tick_counter.py -- mod-free cyclic position tracking.

This formalizes a pattern that predates this toolkit: the original TRTS
paper's `rational_index_tracker` (increment each step, reset to 0 on
reaching the period) is a genuine, working mod-free way to track cyclic
position -- confirmed by tracing that paper's own code, which explicitly
avoids the modulo operator in its generative rule and only uses `%` in
a block marked "for analytical verification only."

Engine (engine.py) already does this implicitly via its local_position
loop. This module names the pattern explicitly so it can be reused
anywhere a cyclic position is needed without reaching for %.
"""

class TickCounter:
    """
    Counts 0, 1, ..., period-1, 0, 1, ... forever, using only increment
    and an equality check against `period` -- no modulo anywhere.
    """
    def __init__(self, period: int):
        if period < 1:
            raise ValueError("period must be >= 1")
        self.period = period
        self.position = 0

    def advance(self) -> int:
        """Advance one step, return the new position (0-indexed)."""
        self.position += 1
        if self.position == self.period:
            self.position = 0
        return self.position

    def is_at_boundary(self) -> bool:
        """True immediately after wrapping back to 0."""
        return self.position == 0
