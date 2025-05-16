# test_calculator_manual.py

import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(3, 3) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(-1, -1) == 1

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculator.divide(10, 0)