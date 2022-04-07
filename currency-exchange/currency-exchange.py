
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
show_currency_exchange()
