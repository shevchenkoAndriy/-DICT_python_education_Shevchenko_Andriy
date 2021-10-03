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






