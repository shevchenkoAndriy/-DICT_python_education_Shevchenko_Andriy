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
        mod = self.correctly_input_command('What do you want to calculate?\n'
                                           'type "n" for number of monthly payments,\n'
                                           'type "a" for annuity monthly payment amount,\n'
                                           'type "p" for loan principal:\n> ',  ("n", "a", "p"))
        if mod == "n":
            loan_principal = self.correct_input_credit("Enter the loan principal: > ")
            monthly_payment = self.is_invalid_value("Enter the monthly payment > ", {"max_value": loan_principal})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_monthly_payment_number(loan_principal, monthly_payment, loan_interest)
        elif mod == "a":
            monthly_payment = self.correct_input_credit("Enter the loan principal: > ")
            number_periods = self.is_invalid_value("Enter the number of periods: >  ", {"max_value": monthly_payment})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_annuity_payment(monthly_payment, number_periods, loan_interest)
        elif mod == "p":
            annuity_payment = self.correct_input_credit("Enter the annuity payment: > ")
            number_periods = self.is_invalid_value("Enter the number of periods: >  ", {"max_value": annuity_payment})
            loan_interest = self.correct_input_percentage("Enter the loan interest: > ")
            self.calc_loan_principal(annuity_payment, number_periods, loan_interest)

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

    def calc_annuity_payment(self, loan_principal, number_periods, loan_interest):
        nominal_rate = self.calc_nominal_rate(loan_interest)
        sum_squared = (1 + nominal_rate) ** number_periods
        monthly_payment = loan_principal * (nominal_rate * sum_squared) / (sum_squared - 1)
        print(f"Your monthly payment = {math.ceil(monthly_payment)}!")

    def calc_loan_principal(self, annuity_payment, number_periods, loan_interest):
        nominal_rate = self.calc_nominal_rate(loan_interest)
        sum_squared = (1 + nominal_rate) ** number_periods
        loan_principal = math.floor(float(annuity_payment / ((nominal_rate * sum_squared) / (sum_squared - 1))))
        print(f"Your loan principal = {loan_principal}!\n")

    def is_invalid_value(self, string, principal):
        value = self.correct_input_credit(string)
        while principal["max_value"] < value:
            print("this value cannot be than high, please enter a value that is less")
            value = self.correct_input_credit(string)
        return value

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


calc = CreditCalculator()
"""1-st"""
# calc.print_status()
"""2-st"""
# calc.credit_to_months()
"""3-st"""
calc.credit_with_annual_payment()
