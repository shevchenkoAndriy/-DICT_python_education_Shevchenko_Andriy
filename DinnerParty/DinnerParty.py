friends_to_party = {}


def add_friend_to_party():
    friends = correct_integer_input("Enter the number of friends joining (including you): > ")
    for i in range(0, friends):
        friend = input("Enter the name of every friend (including you), each on a new line: > ")
        friends_to_party[friend] = 0
    print(friends_to_party)


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


add_friend_to_party()
