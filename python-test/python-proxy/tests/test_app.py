"""Unit tests fixtures."""

from pathlib import Path

import pytest

from conftest import build_proxy


@pytest.fixture(scope='session')
def check_proxy() -> bool:
    """Ensure the proxy is built and up-to-date."""
    return build_proxy('Calculator')


@pytest.mark.parametrize(
    'do, power, operand1, operand2, expected',
    [
        (0, False, 1.5, 2.5, 0.0),
        (0, True, 1.5, 2.5, 4.0),
        (1, True, 1.5, 2.5, -1.0),
    ],
)
def test_function(check_proxy, do, power, operand1, operand2, expected):
    assert check_proxy
    # sys.path must have been updated
    import Calculator
    root = Calculator.Caculator()
    root.Do = do
    root.Power = power
    root.Operand1 = operand1
    root.Operand2 = operand2
    root.call_cycle()
    assert root.Result == expected


