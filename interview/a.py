import math

class ThirtySecondsFormatter:
    """
    Tranform the double into 32 format string
    """
    def __init__(self, money):
        """
        money: double
        :param money:
        :type money:
        """
        self.money = money


    def transform(self):
        """
        the main function to transform money to string type
        return string
        """
        num_part = math.ceil(self.money)
        b = math.modf(self.money)
        decimal_part = b[0]
        numstring = str(num_part)
        string_part = str(decimal_part*31)
        final = numstring + '-' + string_part
        return final


if __name__== "__main__":
    ThirtySecondsFormatter(12.31)
