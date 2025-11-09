def format_name(f_name, l_name):
    title_fname = f_name.title()
    title_lname = l_name.title()
    return f"Your Full Name is {title_fname} {title_lname}"

fName = input("Enter your First Name: ")
lName = input("Enter your Last Name: ")
print(format_name(f_name=fName, l_name=lName))
#Title Case - First Letter Capital + rest letters small
output = len(fName)

def function1(text):
    return text + text

def function2(text):
    return text.title()

output = function2(function1("hello"))
print(output)