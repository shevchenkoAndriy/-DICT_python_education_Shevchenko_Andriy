import random


invalid_symbols = ".,/';[]}{!~`@#$%^&*-_№?+= "


def step1():
    friends_list = add_friends_list()
    print(create_dict(friends_list, 0))


def step2():
    friends_list = add_friends_list()
    discount_for = split_bill_equally(len(friends_list))
    print(create_dict(friends_list, discount_for))


def step3():
    friends_list = add_friends_list()
    add_feature_lucky(friends_list)


def add_feature_lucky(friends):
    selected = correctly_input_command("Do you want to use the"
                                       " \"Who is lucky?\" feature? Write Yes/No: > ", ("yes", "no"))

    if selected == "no":
        lucky = None
        print("No one is going to be lucky")
    else:
        lucky = selecting_lucky(friends)
    return lucky


def correct_integer_input(string):
    user_input = input(string)
    while True:
        try:
            int(float(user_input))
        except ValueError:
            print("Please input number")
            user_input = input(string)
            continue
        user_input = int(user_input)
        if user_input == 0 or user_input < 0:
            print("No one is joining for the party.")
        else:
            break
    return user_input


def split_bill_equally(count):
    total_amount = correct_integer_input("Enter the total amount: > ")
    discount_for = round((total_amount / count), 2)
    return discount_for


def add_friends_list():
    friends_to_party = []
    invited_friends = []
    count = correct_integer_input("Enter the number of friends joining (including you): > ")
    for i in range(count):
        friend = correct_input_name(invited_friends)
        friends_to_party.append(friend)
    return friends_to_party


def create_dict(friends, count):
    friends_to_party = {}
    for friend in friends:
        friends_to_party[friend] = count
    return friends_to_party


def correct_input_name(invited_friends):
    friend = input("Enter the name of every friend (including you), each on a new line:\n> ").lower()
    while True:
        if friend in invited_friends:
            print(f"{friend} has already been invited to dinner.")
            friend = input("> ")
            continue
        elif not friend:
            print("Name cannot be empty")
            friend = input("> ")
        elif friend.isnumeric():
            print("Please input name and not a number")
            friend = input("> ")
        elif friend[0].isnumeric():
            print("Name cannot start with a number")
            friend = input("> ")
        elif friend[0] in invalid_symbols:
            print(f"Name cannot start with \"{list(filter(lambda x: x == friend[0], invalid_symbols))[0]}\"")
            friend = input("> ")
        elif len(friend) < 2:
            print(f"This name is too short")
            friend = input("> ")
        else:
            invited_friends.append(friend)
            friend = f"{friend[0].upper() + friend[1:]}"
            break
    return friend


def correctly_input_command(string, command):
    user_input = input(string)
    while user_input not in command:
        print("please input correctly command")
        user_input = input(string)
    return user_input


def selecting_lucky(friends):
    random_friend = random.choice(friends)
    print(f"{random_friend} is the lucky one!")
    return random_friend


# step1()
# step2()
step3()
