"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def tuple_to_list():
    """Arranging Data for AAA Testing"""
    return 1.0, 2


def test_calculator_add_method():
    """Testing the Calculator-Addition method"""
    assert Calculator.add(tuple_to_list()) == 3


def test_calculator_subtract_method():
    """Testing the Calculator-Subtraction method"""
    assert Calculator.sub(tuple_to_list()) == -3


def test_calculator_multiply_method():
    """Testing the Calculator-Multiplication method"""
    assert Calculator.multi(tuple_to_list()) == 2


def test_calculator_division_method():
    """Testing the Calculator-Division method"""
    assert Calculator.div(tuple_to_list()) == 0.5
