def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3, 5, 6, 2, 1))
# *args - packs any number of tuple items as n Arguments - TUPLE

def calculate(n, **kwargs):      #KeyWord-ARGumentS
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
# **kwargs - make ur own argument and function by keyword - stored as DICTIONARY

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(f"Car Details: Make = {my_car.make} and Model = {my_car.model}")
