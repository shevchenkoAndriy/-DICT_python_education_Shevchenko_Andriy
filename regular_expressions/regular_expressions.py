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
    if regex in '*':
        return True
    elif regex in "?":
        return True
    elif regex in "+":
        return True

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


def repetition(base_list, index, symbol, string_len):
    possibility = []
    if symbol in ["?", "*"]:
        empty_index = base_list[:]
        empty_index[index] = ""
        possibility.append(empty_index)
    if symbol in ["*", "+"]:
        repeated_count = 2
        current_len = len(base_list) + repeated_count - 1

        offset = 0
        if base_list[0] == "^":
            offset += 1
        if base_list[-1] == "$":
            offset += 1

        max_len = string_len + offset

        while current_len <= max_len:
            empty_index = base_list[:]
            index_char = empty_index[index]
            empty_index[index] = index_char * repeated_count
            possibility.append(empty_index)
            repeated_count += 1
            current_len += 1
    return possibility


def regex_v4_helper(base_list, idx_map, max_len):
    scenarios = [base_list]
    for index, meta in idx_map.items():
        current_scenarios = scenarios[:]
        for item in current_scenarios:
            extended_scenarios = repetition(item, index, meta, max_len)
            scenarios.extend(extended_scenarios)

    scenario_str = ["".join(scenario) for scenario in scenarios]

    return scenario_str


def regex_v4(regex, string):
    meta_count = ["?", "*", "+"]
    if all(char not in meta_count for char in regex):
        return regex_v3(regex, string)

    meta_dict = {}

    for i in range(1, len(regex)):
        if regex[i] in meta_count and regex[i - 1] != "\\":
            offset = len(meta_dict)
            meta_dict[i - 1 - offset] = regex[i]

    base_chars = [char for char in regex if char not in meta_count]

    scenarios = regex_v4_helper(base_chars, meta_dict, len(string))

    for item in scenarios:
        current_eval = regex_v3(item, string)
        if current_eval is True:
            return True

    return False


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
    elif "$" in regex:
        return True
    elif "+" in regex:
        return True
    elif "?" in regex:
        return True
    elif "*" in regex:
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
        return

    # fourth_check_level = regex_v3(req_ex, string)
    #
    # if not fourth_check_level:
    #     print(False)
    #
    #     return

    fifth_check_level = regex_v4(req_ex, string)

    if not fifth_check_level:
        print(False)
        return

    print(True)


main()
