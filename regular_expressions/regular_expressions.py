def correct_input_reg_ex():
    user_input = input("Please input regular_expressions|your string > ")
    while True:
        try:
            req_ex, string = user_input.split("|")
            return req_ex, string
        except ValueError:
            print("Incorrect format")
            user_input = input("Please input regular_expressions|your string > ")
            continue


def simple_reg_ex_parser(req_ex, string):
    if req_ex == "":
        return True
    elif string == "":
        return False

    elif req_ex == ".":
        return True

    else:
        return True


def complicated_parser(req_ex, string):
    if len(req_ex) != len(string):
        return False

    for r, s in zip(req_ex, string):
        if r == ".":
            continue
        elif r != s:
            return False

    return True


def main():
    req_ex, string = correct_input_reg_ex()
    first_check_level = simple_reg_ex_parser(req_ex, string)

    if not first_check_level:
        print(False)
        return

    second_check_level = complicated_parser(req_ex, string)
    if not second_check_level:
        print(False)
        return

    print(True)


main()
