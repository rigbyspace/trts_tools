"""
test_rs_toolkit.py -- pytest-style tests for every claim this toolkit
makes. Run with: pytest test_rs_toolkit.py -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from rs_toolkit import (
    ERP, MEDIANT_ABSENCE, FRACTIONAL_ABSENCE,
    eta, boxplus, oplus, psi, psi_advance_a, psi_advance_b,
    suspended, resolve_suspended,
    is_prime_magnitude, sign_of,
    Koppa, Omega,
    Engine,
)


# ---------- ERP type safety ----------

def test_erp_rejects_float():
    with pytest.raises(TypeError):
        ERP(1.0, 2)

def test_erp_rejects_bool_disguised_as_int():
    # type(True) is bool, not int -- the strict `type(n) is not int` check
    # (rather than isinstance) correctly rejects this, even though bool
    # is technically an int subclass. This is deliberate, safer behavior:
    # silently accepting True/False as ERP components would be its own
    # subtle bug source.
    with pytest.raises(TypeError):
        ERP(True, 2)

def test_erp_exact_equality_not_reduction():
    assert ERP(2, 4) != ERP(1, 2)
    assert ERP(2, 4) == ERP(2, 4)


# ---------- Operator identities, confirmed this session ----------

def test_lambda_equals_oplus_with_unity():
    n, d = 37, 58
    lam_direct = ERP(n + d, d)
    lam_via_oplus = oplus(ERP(n, d), ERP(1, 1))
    assert lam_direct == lam_via_oplus

def test_psi_is_involution_squared_full_swap():
    a, b = ERP(5, 9), ERP(3, 4)
    a1, b1 = psi(a, b)
    a2, b2 = psi(a1, b1)
    assert (a2, b2) == (b, a)  # psi^2 = full pair swap

def test_psi_fourth_power_is_identity():
    a, b = ERP(5, 9), ERP(3, 4)
    state = (a, b)
    for _ in range(4):
        state = psi(*state)
    assert state == (a, b)

def test_psi_named_wrappers_match_bare_tuple():
    a, b = ERP(5, 9), ERP(3, 4)
    out = psi(a, b)
    assert psi_advance_a(a, b) == out[0]
    assert psi_advance_b(a, b) == out[1]

def test_eta_not_reducible_to_boxplus_or_oplus_spot_check():
    # full symbolic proof was done separately this session;
    # this is a numeric spot-check that eta's output isn't reproducible
    # by boxplus or oplus with the SAME two inputs
    a = ERP(5, 3)
    assert eta(a) != boxplus(a, a)
    assert eta(a) != oplus(a, a)


# ---------- Zero Logic ----------

def test_suspended_state_has_zero_denominator():
    s = suspended(7)
    assert s.d == 0

def test_resolve_suspended_matches_general_psi_formula():
    s = suspended(5)  # ERP(5, 0)
    other = ERP(3, 4)
    resolved = resolve_suspended(s, other)
    assert resolved == psi(s, other)  # confirmed: no special-casing needed

def test_resolve_suspended_rejects_non_suspended_input():
    with pytest.raises(ValueError):
        resolve_suspended(ERP(5, 1), ERP(3, 4))

def test_evaluate_raises_on_suspended_state():
    s = suspended(5)
    with pytest.raises(ZeroDivisionError):
        s.evaluate()


# ---------- Sign-preserving primality ----------

def test_negative_prime_detected_as_prime():
    assert is_prime_magnitude(-7) is True

def test_negative_prime_sign_untouched():
    n = -7
    is_prime_magnitude(n)
    assert n == -7  # the call must not mutate or shadow the original

def test_negative_composite_not_prime():
    assert is_prime_magnitude(-8) is False

def test_sign_of_all_cases():
    assert sign_of(-5) == -1
    assert sign_of(5) == 1
    assert sign_of(0) == 0


# ---------- Koppa ----------

def test_koppa_starts_at_configurable_absence():
    k_default = Koppa()
    assert k_default.value == MEDIANT_ABSENCE
    k_custom = Koppa(initial=FRACTIONAL_ABSENCE)
    assert k_custom.value == FRACTIONAL_ABSENCE

def test_koppa_deposit_is_pure_addition():
    k = Koppa()
    k.deposit(ERP(3, 4))
    assert k.value == boxplus(MEDIANT_ABSENCE, ERP(3, 4))


# ---------- Engine: the phase-drift regression test ----------

def test_engine_does_not_drift_across_cycle_boundary():
    """
    This is the regression test for the actual bug found this session:
    a hand-rolled 'revert when global_tick % 3 == 0' rule silently
    misaligns with the real local E/M/R roles starting in the second
    cycle, since 11 is not a multiple of 3. Confirms local position 1
    is ALWAYS role 'E', for every cycle, not just the first.
    """
    combine = lambda a, b: boxplus(a, b)
    eng = Engine(ERP(22, 7), ERP(7, 19), combine)
    history = eng.run_cycles(5)
    for tick in history:
        if tick.local_position == 1:
            assert tick.role == 'E'
        if tick.local_position == 11:
            assert tick.role == 'M'
        if tick.local_position in (3, 6, 9):
            assert tick.role == 'R'

def test_engine_boundary_callback_fires_once_per_cycle():
    calls = []
    combine = lambda a, b: boxplus(a, b)
    eng = Engine(ERP(22, 7), ERP(7, 19), combine, on_boundary=lambda e, t: calls.append(t.cycle))
    eng.run_cycles(4)
    assert calls == [1, 2, 3, 4]

def test_engine_return_ticks_record_excluded_value():
    combine = lambda a, b: boxplus(a, b)
    eng = Engine(ERP(22, 7), ERP(7, 19), combine)
    history = eng.run_cycles(1)
    return_ticks = [t for t in history if t.role == 'R']
    assert all(t.excluded is not None for t in return_ticks)


# ---------- TickCounter: mod-free cyclic position ----------

def test_tick_counter_wraps_without_modulo():
    from rs_toolkit import TickCounter
    c = TickCounter(3)
    positions = []
    for _ in range(7):
        positions.append(c.advance())
    assert positions == [1, 2, 0, 1, 2, 0, 1]

def test_tick_counter_boundary_flag():
    from rs_toolkit import TickCounter
    c = TickCounter(3)
    c.advance(); c.advance()
    assert not c.is_at_boundary()
    c.advance()
    assert c.is_at_boundary()


# ---------- precession.py: formalized k-periodic mechanism, re-confirms this session's strongest result ----------

def test_precession_period_matches_k_for_all_tested_values():
    from rs_toolkit import precession_period
    for k in range(3, 10):
        assert precession_period(k) == k

def test_precession_period_rejects_untested_gcd_regime():
    from rs_toolkit import precession_period
    with pytest.raises(NotImplementedError):
        precession_period(11)  # gcd(11,11) != 1 -- untested regime, must not silently claim an answer

def test_run_k_periodic_converges_near_predicted_attractor():
    from rs_toolkit import run_k_periodic, predicted_attractor, ERP
    seq = run_k_periodic(ERP(22, 7), ERP(7, 19), 3, 20)
    ratios = [seq[i].evaluate() / seq[i-1].evaluate() for i in range(1, len(seq))]
    predicted = predicted_attractor(3)
    # the ratio should get close to the predicted attractor at SOME point in its cycle
    closest = min(abs(r - predicted) for r in ratios[-6:])
    assert closest < 0.01


if __name__ == "__main__":
    import subprocess
    subprocess.run([sys.executable, "-m", "pytest", __file__, "-v"])
