import math


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

    def calc_credit_to_months(self):
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

    @staticmethod
    def is_invalid_value(string, principal):
        param = input(string)
        while True:
            try:
                int(param)
            except ValueError:
                print("Please input integer number")
                param = input(string)
                continue
            param = int(param)
            if param == 0:
                print("The entered parameter cannot be equal to 0")
                param = input(string)
                continue
            elif param < 0:
                print("This parameter cannot be negative")
                param = input(string)
            elif param > principal["max_value"]:
                print("This parameter cannot be greater than principal")
                param = input(string)
                continue
            else:
                break
        return param

    @staticmethod
    def calc_monthly_payments_payments(monthly_payment, principal):
        months = math.ceil(principal / monthly_payment)
        print(f"It will take {months} month to repay the loan")

    @staticmethod
    def correct_input_credit(string):
        user_input = input(string)
        while True:
            try:
                int(user_input)
            except ValueError:
                print("Please input integer number")
                user_input = input(string)
                continue
            user_input = int(user_input)
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


calc = CreditCalculator()
"""1-st"""
# calc.print_status()
"""2-st"""
calc.calc_credit_to_months()
