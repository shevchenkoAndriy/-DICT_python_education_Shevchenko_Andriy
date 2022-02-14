from random import choices


def simple_test():
    values = generator(2, 10, ("+", "-", "*"))
    first_number, second_number, action = values
    print(f"{first_number} {action} {second_number} = ")
    user_answer = correct_input_answer("Please input your answer > ")
    true_answer = calc_true_answer(first_number, second_number, action)
    is_correct_answer(user_answer, true_answer)


def generator(a, b, options):
    number_range = range(a, b)
    first_number = choices(number_range)
    second_number = choices(number_range)
    action = choices(options)
    return *first_number, *second_number, *action


def correct_input_answer(string):
    user_input = input(string)
    while True:
        try:
            int(user_input)
        except ValueError:
            print("Incorrect format")
            user_input = input(string)
            continue
        else:
            break
    return int(user_input)


def calc_true_answer(first_number, second_number, action):
    if action == "+":
        return first_number + second_number
    elif action == "-":
        return first_number - second_number
    elif action == "*":
        return first_number * second_number


def is_correct_answer(answer, true_answer):
    if answer == true_answer:
        print("Right!")
    else:
        print("Wrong!")


simple_test()
