"""
ledgers.py -- koppa and Omega.

Koppa's mechanism here is TESTED, not speculative: at an ordinary Return
tick, the TRTS-style recurrence does not sum the previous two terms --
it discards the sum and carries the older term forward instead. The
amount excluded from propagation (the value that WOULD have been added)
is exactly the previous term, confirmed directly this session, and it
can be accumulated purely additively (boxplus) with no subtraction
anywhere. That accumulation is what this Koppa class implements.

Omega's mechanism is NOT tested to the same standard. The "counts
Return/boundary events" behavior is a hypothesis raised in discussion,
not something verified the way Koppa's deposit rule was. It is
implemented here as a plain counter so it is available to build with,
but callers should treat it as CONDITIONAL, not confirmed.
"""

from .erp import ERP, MEDIANT_ABSENCE
from .operators import boxplus


class Koppa:
    """
    Accumulates excluded-sum tension via pure boxplus addition.
    TESTED mechanism (see module docstring).
    """
    def __init__(self, initial: ERP = None):
        # Zero Logic: which absence form is correct depends on which
        # math governs the track this Koppa lives on -- do not hardcode
        # mediant absence as the only valid starting point.
        self.value = initial if initial is not None else MEDIANT_ABSENCE

    def deposit(self, excluded_amount: ERP):
        """Add an excluded amount to the ledger. Pure addition, no subtraction."""
        self.value = boxplus(self.value, excluded_amount)

    def __repr__(self):
        return f"Koppa(value={self.value})"


class Omega:
    """
    CONDITIONAL / not independently tested. Implemented as a simple
    event counter (candidate hypothesis: Omega tracks how many
    Return/boundary events have occurred, rather than accumulating a
    magnitude the way Koppa does). Treat any conclusion drawn from this
    class as provisional until tested with the same rigor as Koppa.
    """
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def __repr__(self):
        return f"Omega(count={self.count}) [CONDITIONAL -- untested mechanism]"


def run_return_tick(history: list, tick_index: int, koppa: 'Koppa'):
    """
    Given a history list (indexed 0..n) of ERPs under the standard
    TRTS-style rule, perform a Return tick at tick_index: the excluded
    amount (history[tick_index - 1]) is deposited into koppa, and the
    propagating value reverts to history[tick_index - 2].
    Returns the new propagating ERP for this tick.
    """
    excluded = history[tick_index - 1]  # rs-guard: allow: list-index bookkeeping, not ERP arithmetic
    koppa.deposit(excluded)
    return history[tick_index - 2]  # rs-guard: allow: list-index bookkeeping, not ERP arithmetic
