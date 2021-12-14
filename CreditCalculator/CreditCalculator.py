

class CreditCalculator:
    test_string = """
    Loan principal: 1000
    Month 1: repaid 250
    Month 2: repaid 250
    Month 3: repaid 500
    The loan has been repaid!
    """

    def print_status(self):
        print(self.test_string)


calc = CreditCalculator()
"""1-st"""
calc.print_status()
