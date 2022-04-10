import requests
import json
from functools import lru_cache


def simple_currency_exchange():
    coins = correct_float_input("Please, enter the number "
                                "of coins you have: > ")
    exchange_rate = correct_float_input("Please, enter the exchange rate: > ")

    print(f"The total amount of dollars: {round(coins * exchange_rate, 2)}")


def show_currency_exchange():
    coin = correct_float_input("Please, enter the number "
                               "of coins you have: > ")
    print(f"I will get {round(coin * 2.87)} ARS from the sale of {coin} coin")
    print(f"I will get {round(coin * 0.6)} HNL from the sale of {coin} coin")
    print(f"I will get {round(coin * 6.87)} AUD from the sale of {coin} coin")
    print(f"I will get {round(coin * 0.73)} MAD from the sale of {coin} coin")


@lru_cache(maxsize=100)
def get_exchange_rate(code):
    print(f"Search... ")
    response = requests.get(f"http://www.floatrates.com/daily/{code}.json")
    if response.ok:
        result = response.json()
        d = result.get("usd").get("rate")
        e = result.get("eur").get("rate")
        return round(d, 2), round(e, 2)

    else:
        return


def step_3():
    code = input("> ").lower()
    results = get_exchange_rate(code)
    if not results:
        print(f'No results found for "{code}"')
        step_3()
        return

    dollar, euro = results
    print(f"""Dollar: {round(dollar, 2)}
Euro: {round(euro, 2)}""")
    step_3()
    ...


def correct_float_input(string):
    user_input = input(string)
    while True:
        try:
            float(user_input)
        except ValueError:
            if "," in user_input:
                user_input = user_input.replace(",", ".")
                continue
            print("Incorrect format")
            user_input = input(string)
            continue
        else:
            break
    return float(user_input)


# simple_currency_exchange()
# show_currency_exchange()
step_3()
