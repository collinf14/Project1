""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication, Division


class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(tuple_to_list):
        """ Defining static add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(tuple_to_list)
        return calculation.get_result()

    @staticmethod
    def sub(tuple_to_list):
        """ Defining static subtract method"""
        calculation = Subtraction.create(tuple_to_list)
        return calculation.get_result()

    @staticmethod
    def multi(tuple_to_list):
        """ Defining static multiply method"""
        calc = Multiplication.create(tuple_to_list)
        return calc.get_result()

    @staticmethod
    def div(tuple_to_list):
        """Defining static divide method"""
        calc = Division.create(tuple_to_list)
        return calc.get_result()
