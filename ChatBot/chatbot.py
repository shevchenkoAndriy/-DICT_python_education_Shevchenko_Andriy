bot_name = "Julia"
birth_year = "2021"
#1
print("Hello! My name is " + bot_name + "." + " I was created in " + birth_year + ".")
#2
print("Please, remind me your name.")
your_name = input("> ")
print("What a great name you have, " + your_name + "!")
#3
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age isп", age, ";", "that's a good time to start programming!")
#4
print("Now I will prove to you that I can count to any number you want.")
i = 0
user_number = int(input(">"))
while i <= user_number:
    print(i, "!")
    i += 1
print("Completed, have a nice day!")
#5
not_pass = True
while not_pass:
    print("let's test your knowledge of python programming.")
    print("Where is the variable declared correctly?")
    print("1) const variable = 10")
    print("2) var variable = 10")
    print("3) variable = 10")
    print("4) let variable = 10")
    answer1 = int(input("> "))
    if answer1 == 3:
        print("Completed, have a nice day!")
        not_pass = False
    else:
        print("Please, try again.")
        continue

not_pass = True
while not_pass:
    print("Which method allows you to convert a string to an integer?")
    print("1) toString()")
    print("2) int()")
    print("3) StrToInt()")
    print("4) integer()")
    answer2 = int(input("> "))
    if answer2 == 2:
        print("Completed, have a nice day!")
        not_pass = False
    else:
        print("Please, try again.")
        continue

not_pass = True
while not_pass:
    print("In which variant is the cycle declared correctly?")
    print("1) for number in numbers:  ")
    print("2) while number <= numbers")
    print("3) for(const number = 0; number>numbers; number+=1)")
    print("4) while (number <= numbers)")
    answer3 = int(input("> "))
    if answer3 == 1:
        print("Completed, have a nice day!")
        not_pass = False
    else:
        print("Please, try again.")
        continue

not_pass = True
while not_pass:
    print("Which method converts a string to lowercase?")
    print("1) toLoverCase()")
    print("2) toLover()")
    print("3) mb_strtolower()")
    print("4) lower()")
    answer1 = int(input("> "))
    if answer1 == 4:
        print("Completed, have a nice day!")
        not_pass = False
    else:
        print("Please, try again.")
        continue

not_pass = True
while not_pass:

    print("In which version is the statement incorrect?")
    print("1) Programmers are not born, but become.")
    print("2) Python is the hardest and most confusing programming language")
    print("3) To compare two values in python use ==")
    print("4) Python is a strongly typed language.")
    answer1 = int(input("> "))
    if answer1 == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        not_pass = False

    else:
        print("Please, try again.")
        continue


