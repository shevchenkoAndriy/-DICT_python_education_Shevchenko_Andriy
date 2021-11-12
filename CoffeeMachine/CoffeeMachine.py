import math


class CoffeeMachine:
    action = ("buy", "fill", "take", "remaining", "exit")
    ingredientsForOne = {"water": 200,
                         "milk": 50,
                         "coffee": 15}

    espresso_action = (250, 16, 1)
    cappuccino_action = (350, 75, 20, 1)
    latte_action = (200, 100, 12, 1)
    cooking_stages = '''
    Starting to make a coffee
    Grinding coffee beans
    Boiling water
    Mixing boiled water with crushed coffee beans
    Pouring coffee into the cup
    Pouring some milk into the cup
    Coffee is ready!'''

    def __init__(self, water=400, milk=540, coffee_beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def stages(self):
        print(self.cooking_stages)

    def calc_ingredients(self):
        coffee_amount = self.correct_integer_input("Write how many cups of coffee you will need: > ")
        print(f"For {coffee_amount} cups of coffee you will need:")
        water, milk, coffee = self.ingredientsForOne.values()
        print(f'''
        For {coffee_amount} cups of coffee you will need:
        {water * coffee_amount} ml of water
        {milk * coffee_amount} ml of milk
        {coffee * coffee_amount} g of coffee beans''')

    def cooking_possibility_check(self):
        water_check = self.correct_float_input("Write how many ml of water the coffee machine has: > ")
        milk_check = self.correct_float_input("Write how many ml of milk the coffee machine has: > ")
        coffee_check = self.correct_float_input("Write how many grams of coffee beans the coffee machine has: > ")
        water, milk, coffee = self.ingredientsForOne.values()
        coffee_amount = self.correct_integer_input("Write how many cups of coffee you will need: > ")
        max_milk = self.calc_max_prod(milk_check, milk)
        max_coffee = self.calc_max_prod(coffee_check, coffee)
        max_water = self.calc_max_prod(water_check, water)
        max_cups_coffee = min(max_milk, max_coffee, max_water)
        if max_cups_coffee == coffee_amount:
            print("Yes, I can make that amount of coffee")
        elif max_cups_coffee > coffee_amount:
            print(f"Yes, I can make that amount of coffee"
                  f" (and even {max_cups_coffee - coffee_amount} more than that)")
        else:
            print(f"No, I can make only {max_cups_coffee} cups of coffee.")

    def availability(self):
        return print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")

    def calc_max_coffee_cups(self, action_coffee):
        if action_coffee == "back":
            return action_coffee
        water = self.water
        milk = self.milk
        coffee_beans = self.coffee_beans
        # cups = self.cups
        if action_coffee == "1":
            necessary_water = 250
            necessary_coffee_beans = 16
            max_coffee = self.calc_max_prod(coffee_beans, necessary_coffee_beans)
            # print(calc_max_prod(coffee_beans, necessary_coffee_beans))
            max_water = self.calc_max_prod(water, necessary_water)
            # print(min(max_coffee, max_water))
            return min(max_coffee, max_water)

        elif action_coffee == "2":
            necessary_water = 350
            necessary_milk = 75
            necessary_coffee_beans = 20
            max_milk = self.calc_max_prod(milk, necessary_milk)
            max_coffee = self.calc_max_prod(coffee_beans, necessary_coffee_beans)
            max_water = self.calc_max_prod(water, necessary_water)
            return min(max_milk, max_coffee, max_water)

        elif action_coffee == "3":
            necessary_water = 200
            necessary_milk = 100
            necessary_coffee_beans = 12
            max_milk = self.calc_max_prod(milk, necessary_milk)
            max_coffee = self.calc_max_prod(coffee_beans, necessary_coffee_beans)
            max_water = self.calc_max_prod(water, necessary_water)
            return min(max_milk, max_coffee, max_water)

    @staticmethod
    def reload_function(function):
        function()

    @staticmethod
    def correct_integer_input(string):
        user_input = input(string)
        while True:
            try:
                int(user_input)
            except ValueError:
                print("Please input integer number")
                user_input = input(string)
                continue
            else:
                break
        return int(user_input)

    @staticmethod
    def correct_float_input(string):
        user_input = input(string)
        while True:
            try:
                float(user_input)
            except ValueError:
                print("Please input number")
                user_input = input(string)
                continue
            else:
                break
        return float(user_input)

    @staticmethod
    def calc_max_prod(ingredient, ingredients_required_for_one):
        return math.trunc(ingredient / ingredients_required_for_one)

    @staticmethod
    def correctly_input_command(string, command):
        user_input = input(string)
        while user_input not in command:
            print("please input correctly command")
            user_input = input(string)
        return user_input


# cm1 = CoffeeMachine()
# cm1.stages()


# cm2 = CoffeeMachine()
# cm2.calc_ingredients()


# cm3 = CoffeeMachine()
# cm3.cooking_possibility_check()


class CoffeeMachine4 (CoffeeMachine):

    def coffee_machine4(self):
        self.availability()
        action = self.correctly_input_command("Write action (buy, fill, take): > ", self.action)
        if action == "remaining" or action == "exit":
            print("This version does not support this feature")
        self.main_menu(action)
        self.coffee_machine4()

    def enable_purchase_mode(self, action):
        if action == "1":
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            self.money += 4
        elif action == "2":
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
        elif action == "3":
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
        elif action == "back":
            return action

    def buy_mode(self):
        action = self.correctly_input_command("What do you want to buy?"
                                              " 1 - espresso, 2 - latte, 3 - cappuccino,"
                                              " back – to main menu: > ", ("1", "2", "3", "back"))
        max_cups = self.calc_max_coffee_cups(action)
        if max_cups == "back":
            return
        if max_cups < 1:
            print("Sorry I don't have enough ingredients")
        elif max_cups >= 1:
            self.enable_purchase_mode(action)
            print("I have enough resources, making you a coffee!")

    def fill_mode(self):
        selected_command = self.correctly_input_command("What do you want to add?"
                                                        " (1-water, 2-milk, 3-beans, 4-cups): > ",
                                                        ("1", "2", "3", "4"))
        self.fill_menu(selected_command)

    def take_mod(self):
        revenue = self.money
        self.money -= revenue
        print(f"I gave you {revenue}")

    def main_menu(self, action):
        if action == "buy":
            self.buy_mode()
        elif action == "fill":
            self.fill_mode()
        elif action == "take":
            self.take_mod()

    def fill_menu(self, selected_fill):
        if selected_fill == "1":
            water_add = self.correct_float_input("Write how many ml of water you want to add: > ")
            self.water += water_add

        elif selected_fill == "2":
            milk_add = self.correct_float_input("Write how many ml of milk you want to add: > ")
            self.milk += milk_add

        elif selected_fill == "3":
            coffee_add = self.correct_float_input("Write how many grams of coffee beans you want to add: > ")
            self.coffee_beans = coffee_add

        elif selected_fill == "4":
            cups_add = self.correct_integer_input("Write how many disposable coffee cups you want to add: > ")
            self.cups = cups_add

    def fill_coffee_mach(self, selected_command, selected_fill):
        if selected_command == "1":
            self.water += selected_fill
        elif selected_command == "2":
            self.milk += selected_fill
        elif selected_command == "3":
            self.coffee_beans += selected_fill
        elif selected_command == "4":
            self.cups += selected_fill


# cm4 = CoffeeMachine4(water=400, milk=540, coffee_beans=120, cups=9, money=550)
# cm4.coffee_machine4()


class CoffeeMachine5 (CoffeeMachine4):
    def coffee_machine5(self):
        action = self.correctly_input_command("Write action (buy, fill, take, remaining, exit): > ", self.action)
        if action == "remaining":
            self.availability()
        elif action == "exit":
            return
        self.main_menu(action)
        self.coffee_machine5()


cm5 = CoffeeMachine5(water=400, milk=540, coffee_beans=120, cups=9, money=550)
cm5.coffee_machine5()
