# age = int(input("How old are you?"))
#
# if age > 18:
#     print("You can drive at age {age}.")
#Absence of f string and missing ident in if...

#Exception Handling
try:
    age = int(input("How old are you?"))
except ValueError:  #identify the exceptName during error in console
    print("You Have Typed invalid character!. Type an Integer")
    age = int(input("How old are you?"))

if age >= 21:
    print(f"Your {age} is legal for drinking")
else:
    print(f"Your {age} is illegal for drinking")
