"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication, Division


def test_calc_multiplication_instance():
    """Testing for instance of multiplication"""
    tuple_to_list = (1, 2)
    calc = Multiplication.create(tuple_to_list)
    assert isinstance(calc, Multiplication)


def test_calc_subtraction_instance():
    """Testing for instance of subtraction"""
    tuple_to_list = (1, 2)
    calc = Subtraction.create(tuple_to_list)
    assert isinstance(calc, Subtraction)


def test_calc_addition_instance():
    """Testing for instance of addition"""
    tuple_to_list = (1, 2)
    calc = Addition.create(tuple_to_list)
    assert isinstance(calc, Addition)


def test_calc_division_instance():
    """Testing for instance of division"""
    tuple_to_list = (1, 2)
    calc = Division.create(tuple_to_list)
    assert isinstance(calc, Division)


def test_calculation_add_get_result_method():
    """Testing the get result of the Addition Class"""
    tuple_to_list = (1, 2)
    calc = Addition.create(tuple_to_list)
    assert calc.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the get result of the Subtraction Class"""
    tuple_to_list = (1, 2)
    calc = Subtraction.create(tuple_to_list)
    assert calc.get_result() == -3


def test_calculation_multiply_get_result_method():
    """Testing the get result of the Multiplication Class"""
    tuple_to_list = (1, 2)
    calc = Multiplication.create(tuple_to_list)
    assert calc.get_result() == 2


def test_calculation_division_get_result_method():
    """Testing the get result of the Division Class"""
    tuple_to_list = (2, 4)
    calc = Division.create(tuple_to_list)
    assert calc.get_result() == 0.125
