def add(n1, n2):
    return round(float(n1 + n2), 1)

#TODO 1: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return round(float(n1 - n2), 1)

def multiply(n1, n2):
    return round(float(n1 * n2), 1)

def divide(n1, n2):
    return n1 / n2

yes_condition = True

#TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
from art import logo
print(logo)

fNum = int(input("What's the first Number?: "))

    #TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
while yes_condition:
    calculator = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }


    for keys in calculator:
        print(keys)

    opern = input("Pick an operation: ")
    lNum = int(input("What's the next num?: "))

    for result in calculator:
        if opern == '+':
            result = calculator['+'](fNum, lNum)
        elif opern == '-':
            result = calculator['-'](fNum, lNum)
        elif opern == '*':
            result = calculator['*'](fNum, lNum)
        elif opern == '/':
            result = calculator['/'](fNum, lNum)
        else:
            result = 0.0

    if opern == '+':
        print(f"{round(float(fNum), 1)} + {round(float(lNum),1)} = {result}")
    elif opern == '-':
        print(f"{round(float(fNum), 1)} - {round(float(lNum), 1)} = {result}")
    elif opern == '*':
        print(f"{round(float(fNum), 1)} * {round(float(lNum), 1)} = {result}")
    elif opern == '/':
        print(f"{round(float(fNum), 1)} / {round(float(lNum), 1)} = {result}")
    else:
        print(f"{round(float(fNum), 1)} undefined {round(float(lNum), 1)} = {result}")

    option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'AC' to exit: ").lower()

    if option == 'y':
        yes_condition = True
        fNum = result

    elif option == 'n':
        print("\n" * 20)
        print(logo)
        fNum = int(input("What's the first Number?: "))
        yes_condition = True

    else:
        yes_condition = False