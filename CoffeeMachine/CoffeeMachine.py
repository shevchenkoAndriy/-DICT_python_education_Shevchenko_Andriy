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
        coffee_amount = correct_input("Write how many cups of coffee you will need: > ")
        print(f"For {coffee_amount} cups of coffee you will need:")
        water, milk, coffee = self.ingredientsForOne.values()
        print(f'''
        For {coffee_amount} cups of coffee you will need:
        {water * coffee_amount} ml of water
        {milk * coffee_amount} ml of milk
        {coffee * coffee_amount} g of coffee beans''')


"""
secondary function
"""


def correct_input(string):
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


# cm1 = CoffeeMachine()
# cm1.stages()


cm2 = CoffeeMachine()
cm2.calc_ingredients()
