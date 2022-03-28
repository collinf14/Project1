"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calc_op_add():
    """Testing the Addition Part of the Calculator"""
    assert Addition.add(10, 1.7) == 11.7


def test_calc_op_subtract():
    """Testing the Subtraction Part of the Calculator"""
    assert Subtraction.sub(22.2, 11.1) == 11.1


def test_calc_op_multiply():
    """Testing the Multiplication Part of the Calculator"""
    assert Multiplication.multi(1.1, 4) == 4.4


def test_calc_op_division():
    """Testing the Division (nonzero) Part of the Calculator"""
    assert Division.div(11, 2) == 5.5


def test_calc_op_division_zero():
    """Testing the Division (zero) Part of the Calculator"""
    assert Division.div(11.4, 0) == 0
