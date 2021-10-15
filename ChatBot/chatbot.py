questions = [
    {
        "value": "Where is the variable declared correctly?",
        "answers": {
            "option1": "1) const variable = 10",
            "option2": "2) var variable = 10",
            "option3": "3) variable = 10",
            "option4": "4) let variable = 10",

        },
        "right_answer": 3
    },
    {
        "value": "Which method allows you to convert a string to an integer?",
        "answers": {
            "option1": "1) toString()",
            "option2": "2) int()",
            "option3": "3) StrToInt()",
            "option4": "4) integer()",
        },
        "right_answer": 2
    },
    {
        "value": "In which variant is the cycle declared correctly?",
        "answers": {
            "option1": "1) for number in numbers:",
            "option2": "2) while number <= numbers",
            "option3": "3) for(const number = 0; number>numbers; number+=1)",
            "option4": "4) while (number <= numbers)",
        },
        "right_answer": 1
    },
    {
        "value": "Which method converts a string to lowercase?",
        "answers": {
            "option1": "1) toLoverCase()",
            "option2": "2) toLover()",
            "option3": "3) mb_strtolower()",
            "option4": "4) lower()",
        },
        "right_answer": 4
    },
    {
        "value": "In which version is the statement incorrect?",
        "answers": {
            "option1": "1) Programmers are not born, but become.",
            "option2": "2) Python is the hardest and most confusing programming language",
            "option3": "3) To compare two values in python use ==",
            "option4": "4) Python is a strongly typed language.",
        },
        "right_answer": 3
    },
]


def hello(bot_name, birth_year):
    print("Hello! My name is " + bot_name + "." + " I was created in " + birth_year + ".")


def input_name():
    print("Please, remind me your name.")
    your_name = input("> ")
    print("What a great name you have, " + your_name + "!")


def age_calc():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input("> "))
    remainder5 = int(input("> "))
    remainder7 = int(input("> "))
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print("Your age isп", age, ";", "that's a good time to start programming!")


def number_calc():
    print("Now I will prove to you that I can count to any number you want.")
    i = 0
    user_number = int(input(">"))
    while i <= user_number:
        print(i, "!")
        i += 1
    print("Completed, have a nice day!")


def test():
    print("let's test your knowledge of python programming.")
    for question in questions:
        not_pass = True
        while not_pass:
            print(question["value"])
            print(question["answers"]["option1"])
            print(question["answers"]["option2"])
            print(question["answers"]["option3"])
            print(question["answers"]["option4"])
            answer = int(input("> "))
            if answer == question["right_answer"]:
                print("Completed, have a nice day!")
                not_pass = False
            else:
                print("Please, try again.")
                continue


hello("Julia", "2021")
input_name()
age_calc()
number_calc()
test()
