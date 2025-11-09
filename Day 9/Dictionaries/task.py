programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The Action of doing something over and over again.",
    404: "The error 404 or “Page Not Found” represents that the server cannot find a "
         "web page request by the user."
}

# print(programming_dictionary["Function"])
# print(programming_dictionary[404])
# print(programming_dictionary) #print all dictionary items including braces {}

empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    print(key) #just print the 'KEY'
    print(programming_dictionary[key]) #just print the 'VALUE'