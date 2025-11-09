#Project 5 - Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
password = ""

for char in range(1, nr_letters + 1):
    ranChar = random.choice(letters)
    password += ranChar

for syms in range(1, nr_symbols + 1):
    ranSyms = random.choice(symbols)
    password += ranSyms

for nums in range(1, nr_numbers + 1):
    ranNums = random.choice(numbers)
    password += ranNums

print("Thus by Easy Level - Password Generated: " + password)

#Hard Level
passwordList = []

for ch in range(0, nr_letters):
    passwordList.append(random.choice(letters))

for syb in range(0, nr_symbols):
    passwordList.append(random.choice(symbols))

for no in range(0, nr_numbers):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList) #shuffle alphanumeric list randomly

hardPw = ""
for anything in passwordList:
    hardPw += anything
print("Thus by Hard Level - Password Generated: " + hardPw)
