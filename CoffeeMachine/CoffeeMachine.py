class CoffeeMachine:
    ingredients = ("coffee", "milk", "sugar")
    drinks = ("espresso", "cappuccino", "latte")
    cooking_stages = '''
    Starting to make a coffee
    Grinding coffee beans
    Boiling water
    Mixing boiled water with crushed coffee beans
    Pouring coffee into the cup
    Pouring some milk into the cup
    Coffee is ready!'''


cm1 = CoffeeMachine()
print(cm1.cooking_stages)
