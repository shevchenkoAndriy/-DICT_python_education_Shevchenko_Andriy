from random import choices


def simple_exercise():
    first_number, second_number, action = generator(2, 10, ("+", "-", "*"))
    print(f"{first_number} {action} {second_number} = ")
    user_answer = correct_input_answer("Please input your answer > ")
    true_answer = calc_true_answer(first_number, second_number, action)
    return is_correct_answer(user_answer, true_answer)


def exponentiation_exercise():
    number_range = range(11, 29)
    number, = random_number(number_range)
    print(f"{number} ^ 2 = ")
    correct_answer = number ** 2
    user_answer = correct_input_answer("Please input your answer > ")
    return is_correct_answer(user_answer, correct_answer)


def generator(a, b, options):
    number_range = range(a, b)
    first_number = random_number(number_range)
    second_number = random_number(number_range)
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


def random_number(number_range):
    number = choices(number_range)
    return *number,


def is_correct_answer(answer, true_answer):
    if answer == true_answer:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def run_test(iteration_number, exercise):
    correct_answer = 0
    counter = 1
    while counter <= iteration_number:
        correct_answer += exercise()
        counter += 1
    # print(f"Your mark is {correct_answer}/{iteration_number}.")
    return correct_answer, iteration_number


def correctly_input_command(string, command):
    user_input = input(string)
    while user_input not in command:
        print("Please input correctly mode")
        user_input = input(string)
    return user_input


def test_menu():
    correct_answer = 0
    iteration_number = 0
    selected_mode = correctly_input_command(
        f"""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n> """, ("1", "2"))
    if selected_mode == "1":
        correct_answer, iteration_number = run_test(5, simple_exercise)

    elif selected_mode == "2":
        correct_answer, iteration_number = run_test(5, exponentiation_exercise)
    save_results = correctly_input_command(f"Your mark is {correct_answer}/{iteration_number}."
                                           f" Would you like to save the result?\n"
                                           f"Enter yes or no > ", ("yes", "no"))
    if save_results == "yes":
        user_name = input("Please input name > ").strip()
        user_name = user_name if user_name else "No name"
        save_progress(user_name,
                      f"{correct_answer}/{iteration_number}",
                      selected_mode,
                      )


def save_progress(name, progress, mod):
    selected_mod = mod
    if selected_mod == "1":
        selected_mod = "1 (simple operations with numbers 2-9)."
    elif selected_mod == "2":
        selected_mod = "2 (integral squares of 11-29)."

    file_result = open("results.txt", "w")
    file_result.write(f"{name}: {progress} in {selected_mod}")
    file_result.close()


# simple_exercise() #st-1
# run_test(5, simple_exercise)
test_menu()
