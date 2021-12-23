import math
from sys import argv
import argparse


class CreditCalculator:

    def __init__(self):
        self.type = ""
        self.monthly_payment = 0
        self.loan_principal = 0
        self.loan_interest = 0
        self.periods_count = 0
        # self.error = ""

    test_string = """
    Loan principal: 1000
    Month 1: repaid 250
    Month 2: repaid 250
    Month 3: repaid 500
    The loan has been repaid!
    """

    def show_settings(self):
        print(f"""
        self.type = {self.type} 
        self.monthly_payment = {self.monthly_payment}
        self.loan_principal = {self.loan_principal} 
        self.periods_count = {self.periods_count} 
        self.loan_interest = {self.loan_interest} 
        """)

    def print_status(self):
        print(self.test_string)

    def loan_calc_mode_selection(self):
        args = self.parse_argument()
        self.init_parameters(args)
        self.show_settings()
        if not self.is_incorrect_parameters():
            print("Incorrect parameters")
        elif self.type == "diff":
            self.calc_diff_credit()
        elif self.type == "annuity":
            self.credit_with_annual_payment()
        else:
            print("FAC")

    def init_parameters(self, parameters):
        self.type = parameters.type
        self.monthly_payment = parameters.payment
        self.loan_principal = parameters.principal
        self.periods_count = parameters.periods
        self.loan_interest = parameters.interest

    def is_incorrect_parameters(self):
        if self.type != "annuity" and self.type != "diff":
            return
        elif self.type == "diff" and self.monthly_payment:
            return
        elif not self.loan_interest:
            return
        elif len(argv) < 4:
            return
        elif not self.is_positive_value():
            return
        else:
            return True

    def credit_to_months(self):
        principal = self.correct_input_credit("Enter the loan principal: > ")
        mod = self.correctly_input_command('What do you want to calculate?\n'
                                           'type "m" – for number of monthly payments,\n'
                                           'type "p" – for the monthly payment: > ', ("m", "p"))
        if mod == "m":
            monthly_payment = self.is_invalid_value("Enter the monthly payment: > ", {"max_value": principal})
            self.calc_monthly_payments_payments(monthly_payment, principal)
        elif mod == "p":
            months = self.is_invalid_value("Enter the number of months: > ", {"max_value": principal})
            self.calc_payment(months, principal)

    def credit_with_annual_payment(self):

        if self.loan_principal and self.monthly_payment and self.loan_interest:
            periods_count = self.calc_monthly_payment_number(self.loan_principal,
                                                             self.monthly_payment, self.loan_interest)
            self.calc_overpayment(periods_count, self.monthly_payment, self.loan_principal)
        elif self.loan_principal and self.periods_count and self.loan_interest:
            annuity_payment = self.calc_annuity_payment(self.loan_principal, self.periods_count, self.loan_interest)
            self.calc_overpayment(annuity_payment, self.periods_count, self.loan_principal)
        elif self.monthly_payment and self.periods_count and self.loan_interest:
            loan_principal = self.calc_loan_principal(self.monthly_payment, self.periods_count, self.loan_interest)
            self.calc_overpayment(self.monthly_payment, self.periods_count, loan_principal)

    def calc_diff_credit(self):
        nominal_rate = self.calc_nominal_rate(self.loan_interest)
        overpayment = 0
        for count in range(1, math.ceil(self.periods_count) + 1):
            dif_payment = math.ceil((self.loan_principal / self.periods_count) + nominal_rate *
                                    (self.loan_principal - ((self.loan_principal * (count - 1)) / self.periods_count)))
            overpayment += dif_payment - self.loan_principal // self.periods_count
            print(f"Month {count}: payment is {dif_payment}")
        print(f"\nOverpayment = {math.ceil(overpayment)}")

    def credit_input_version(self):
        mod = self.correctly_input_command('What do you want to calculate?\n'
                                           'type "n" for number of monthly payments,\n'
                                           'type "a" for annuity monthly payment amount,\n'
                                           'type "p" for loan principal:\n> ', ("n", "a", "p"))
        if mod == "n":
            loan_principal = self.correct_input_credit("Enter the loan principal: > ")
            monthly_payment = self.is_invalid_value("Enter the monthly payment > ", {"max_value": loan_principal})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_monthly_payment_number(loan_principal, monthly_payment, loan_interest)
        elif mod == "a":
            loan_principal = self.correct_input_credit("Enter the loan principal: > ")
            periods_count = self.is_invalid_value("Enter the number of periods: >  ", {"max_value": loan_principal})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_annuity_payment(loan_principal, periods_count, loan_interest)
        elif mod == "p":
            annuity_payment = self.correct_input_credit("Enter the annuity payment: > ")
            periods_count = self.is_invalid_value("Enter the number of periods: >  ", {"max_value": annuity_payment})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_loan_principal(annuity_payment, periods_count, loan_interest)

    def calc_monthly_payment_number(self, loan_principal, monthly_payment, loan_interest):
        nominal_rate = self.calc_nominal_rate(loan_interest)
        argument = (monthly_payment / (monthly_payment - nominal_rate * loan_principal))
        base = nominal_rate + 1
        number_months = math.ceil(math.log(argument, base))
        number_monthly_payment = number_months / 12
        months = (number_monthly_payment - math.floor(number_monthly_payment)) * 12
        if math.floor(number_monthly_payment) != 0 and math.floor(months) != 0:
            print(f"It will take {math.floor(number_monthly_payment)}"
                  f" years and {math.ceil(months)} months to repay this loan!")
        elif math.floor(months) == 0:
            print(f"It will take {math.floor(number_monthly_payment)} years to repay this loan!")
        elif math.floor(number_monthly_payment) == 0:
            print(f"It will take {math.ceil(months)} months to repay this loan!")
        return number_months

    def calc_annuity_payment(self, loan_principal, number_periods, loan_interest):
        nominal_rate = self.calc_nominal_rate(loan_interest)
        sum_squared = (1 + nominal_rate) ** number_periods
        monthly_payment = loan_principal * (nominal_rate * sum_squared) / (sum_squared - 1)
        print(f"Your monthly payment = {math.ceil(monthly_payment)}!")
        return math.ceil(monthly_payment)

    def calc_loan_principal(self, annuity_payment, number_periods, loan_interest):
        nominal_rate = self.calc_nominal_rate(loan_interest)
        sum_squared = (1 + nominal_rate) ** number_periods
        loan_principal = math.floor(float(annuity_payment / ((nominal_rate * sum_squared) / (sum_squared - 1))))
        print(f"Your loan principal = {loan_principal}!\n")
        return loan_principal

    def is_invalid_value(self, string, principal):
        value = self.correct_input_credit(string)
        while principal["max_value"] < value:
            print("this value cannot be than high, please enter a value that is less")
            value = self.correct_input_credit(string)
        return value

    def is_positive_value(self):
        parameters = [self.monthly_payment, self.loan_principal, self.periods_count, self.loan_interest]
        parameters = list(filter(lambda x: x, parameters))
        parameters = list(filter(lambda x: x < 0, parameters))
        if not parameters:
            return True

    @staticmethod
    def calc_monthly_payments_payments(monthly_payment, principal):
        months = math.ceil(principal / monthly_payment)
        print(f"It will take {months} month to repay the loan")

    @staticmethod
    def correct_input_credit(string):
        user_input = input(string)
        while True:
            try:
                float(user_input)
            except ValueError:
                if user_input.find(",") != -1:
                    user_input = user_input.replace(",", ".")
                    continue
                print("Please input number")
                user_input = input(string)
                continue
            user_input = float(user_input)
            if user_input == 0:
                print("The entered parameter cannot be equal to 0")
                user_input = input(string)
                continue
            elif user_input < 0:
                print("This parameter cannot be negative")
                user_input = input(string)
            else:
                break
        return user_input

    @staticmethod
    def correctly_input_command(string, command):
        user_input = input(string)
        while user_input not in command:
            print("please input correctly command")
            user_input = input(string)
        return user_input

    @staticmethod
    def calc_payment(months, principal):
        payment = math.ceil(principal / months)
        last_payment = principal - ((months - 1) * payment)
        if principal < months * 2 or last_payment < 0:
            payment = principal / months
            print(f"Your monthly payment = {round(payment)}")
            return
        if last_payment == payment:
            print(f"Your monthly payment = {payment}")
        else:
            print(f"Your monthly payment = {payment} and the last payment = {last_payment}")

    @staticmethod
    def correct_input_percentage(string):
        user_input = input(string)
        while True:
            try:
                float(user_input)
            except ValueError:
                if user_input.find(",") != -1:
                    user_input = user_input.replace(",", ".")
                    continue
                print("please input correct interest")
                user_input = input(string)
                continue
            user_input = float(user_input)
            if user_input <= 0:
                print("percentage cannot be zero less than zero")
                user_input = input(string)
                continue
            if user_input > 60:
                print("please input number slightly less")
                user_input = input(string)
            else:
                break
        return user_input

    @staticmethod
    def calc_nominal_rate(loan_interest):
        return loan_interest * 0.01 / 12

    @staticmethod
    def parse_argument():
        parser = argparse.ArgumentParser()
        parser.add_argument('--type', type=str)
        parser.add_argument('--payment', type=float)
        parser.add_argument('--principal', type=float)
        parser.add_argument('--periods', type=float)
        parser.add_argument('--interest', type=float)
        return parser.parse_args()

    @staticmethod
    def calc_overpayment(factor1, factor2, minuend):
        print(f"{math.ceil((factor1 * factor2) - minuend)}")


calc = CreditCalculator()
"""1-st"""
# calc.print_status()
"""2-st"""
# calc.credit_to_months()
"""3-st"""
# calc.credit_input_version()
""" 
    python3.10 CreditCalculator/CreditCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
    python3.10 CreditCalculator/CreditCalculator.py --type=diff --principal=1000000 --periods=10 --interest=10
    python3.10 CreditCalculator/CreditCalculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
    python3.10 CreditCalculator/CreditCalculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
    errors setting:
    python3.10 CreditCalculator/CreditCalculator.py --principal=1000000 --periods=60 --interest=10
    python3.10 CreditCalculator/CreditCalculator.py --type=diff --principal=1000000 --interest=10 --payment=100000
    python3.10 CreditCalculator/CreditCalculator.py --type=annuity --principal=100000 --payment=10400 --periods=8
    python3.10 CreditCalculator/CreditCalculator.py --type=annuity --principal=1000000 --payment=104000
    python3.10 CreditCalculator/CreditCalculator.py --type=diff --principal=30000 --periods=-14 --interest=10

   """
calc.loan_calc_mode_selection()
