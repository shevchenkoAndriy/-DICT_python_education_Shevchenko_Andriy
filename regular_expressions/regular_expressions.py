def simple_reg_ex_parser():
    req_ex, string = input("Please input regular_expressions|your string > ").split("|")
    if req_ex == "":
        return True
    elif string == "":
        return False

    elif req_ex == ".":
        return True
    else:
        return req_ex == string


print(simple_reg_ex_parser())

