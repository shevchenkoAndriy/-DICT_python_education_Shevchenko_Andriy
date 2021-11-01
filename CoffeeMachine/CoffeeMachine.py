import math


class CoffeeMachine:
    ingredientsForOne = {"water": 200,
                         "milk": 50,
                         "coffee": 15}

    drinks = ("espresso", "cappuccino", "latte")
    cooking_stages = '''
    Starting to make a coffee
    Grinding coffee beans
    Boiling water
    Mixing boiled water with crushed coffee beans
    Pouring coffee into the cup
    Pouring some milk into the cup
    Coffee is ready!'''

    def stages(self):
        print(self.cooking_stages)

    def calc_ingredients(self):
        coffee_amount = correct_integer_input("Write how many cups of coffee you will need: > ")
        print(f"For {coffee_amount} cups of coffee you will need:")
        water, milk, coffee = self.ingredientsForOne.values()
        print(f'''
        For {coffee_amount} cups of coffee you will need:
        {water * coffee_amount} ml of water
        {milk * coffee_amount} ml of milk
        {coffee * coffee_amount} g of coffee beans''')

    def cooking_possibility_check(self):
        water_check = correct_float_input("Write how many ml of water the coffee machine has: > ")
        milk_check = correct_float_input("Write how many ml of milk the coffee machine has: > ")
        coffee_check = correct_float_input("Write how many grams of coffee beans the coffee machine has: > ")
        water, milk, coffee = self.ingredientsForOne.values()
        coffee_amount = correct_integer_input("Write how many cups of coffee you will need: > ")
        max_milk = calc_max_prod(milk_check, milk)
        max_coffee = calc_max_prod(coffee_check, coffee)
        max_water = calc_max_prod(water_check, water)
        max_cups_coffee = min(max_milk, max_coffee, max_water)
        if max_cups_coffee == coffee_amount:
            print("Yes, I can make that amount of coffee")
        elif max_cups_coffee > coffee_amount:
            print(f"Yes, I can make that amount of coffee"
                  f" (and even {max_cups_coffee - coffee_amount} more than that)")
        else:
            print(f"No, I can make only {max_cups_coffee} cups of coffee.")


"""
secondary function
"""


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


def calc_max_prod(ingredient, ingredients_required_for_one):
    return math.trunc(ingredient / ingredients_required_for_one)


# cm1 = CoffeeMachine()
# cm1.stages()


cm2 = CoffeeMachine()
cm2.calc_ingredients()


cm3 = CoffeeMachine()
cm3.cooking_possibility_check()
