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


def regex_v3(regex: str, string):
    if regex.startswith("^"):
        regex = regex.replace("^", "")
        temp_regex = regex.replace("$", "")
        for i in range(len(temp_regex)):
            if temp_regex[i] != "." and temp_regex[i] != string[i]:
                return False

    if regex.endswith("$"):
        regex = regex.replace("$", "")
        for i in range(-1, -1 - len(regex), -1):
            if regex[i] != "." and regex[i] != string[i]:
                return False

    return unequal_len_regex(regex, string)


def equal_len(regex: str, literal: str) -> bool:
    if regex == "":
        return True
    elif literal == "":
        return False
    elif regex[0] != "." and regex[0] != literal[0]:
        return False
    else:
        return equal_len(regex[1:], literal[1:])


def different_len(regex: str, literal: str) -> bool:
    if "^" in regex:
        return True
    if "$" in regex:
        return True
    equal_len_matches: bool = equal_len(regex, literal)

    if equal_len_matches:
        return True
    elif literal == "":
        return False
    else:
        return different_len(regex, literal[1:])


def regex_recursion(regex, string):
    if regex == "":
        return True
    elif string == "":
        return False
    elif regex[0] != "." and regex[0] != string[0]:
        return False
    else:
        return regex_recursion(regex[1:], string[1:])


def unequal_len_regex(regex, string):
    found_match = regex_recursion(regex, string)

    if found_match:
        return True
    elif string == "":
        return False
    else:
        return unequal_len_regex(regex, string[1:])


def complicated_parser(req_ex, string):
    if len(req_ex) != len(string):
        return True

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

    third_check_level = different_len(req_ex, string)

    if not third_check_level:
        print(False)
        print("here")
        return

    fourth_check_level = regex_v3(req_ex, string)

    if not fourth_check_level:
        print(False)
        return

    print(True)


main()
