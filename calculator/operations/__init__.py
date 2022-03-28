""" Classes for each Operation"""


class Addition:
    """ Addition Class"""

    @staticmethod
    def add(val_1, val_2):
        """ Addition Method"""
        return val_1 + val_2


class Subtraction:
    """ Subtraction Class"""

    @staticmethod
    def sub(val_1, val_2):
        """ Subtraction Method"""
        return val_1 - val_2


class Multiplication:
    """ Multiplication Class"""

    @staticmethod
    def multi(val_1, val_2):
        """ Multiplication Method"""
        return val_1 * val_2


class Division:
    """Division Class"""

    @staticmethod
    def div(val_1, val_2):
        """Division Method"""
        if val_2 == 0:
            return 0
        else:
            return val_1 / val_2
