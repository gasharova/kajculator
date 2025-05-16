# test_calculator_auto.py


# automatic testing:

import calculator
import pytest

def test_generated_1():
    assert calculator.add(0, 0) == 0

def test_generated_2():
    assert calculator.subtract(-10, -10) == 0

def test_generated_3():
    assert calculator.multiply(100, 0) == 0

def test_generated_4():
    with pytest.raises(ValueError):
        calculator.divide(123, 0)