# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"You Residence is at {location}")

greet_with_name("Atharva Lotankar", "Mumbai")#positional arg

greet_with_name(location = "Mumbai", name="Atharva Lotankar") #keyword arg
