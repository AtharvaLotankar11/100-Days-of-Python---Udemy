#new_list = [new_item for item in list] - LIST COMPREHENSION

#Increment by 1 in new_list
numbers = [1, 2, 3, 4]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

#Indivisualise string to letter-by-letter
name = "Atharva"
letter_list = [letter for letter in name]
print(letter_list)

#Create a new list from a range, where list items are double the values in the range
#currRange (1, 5) = 1, 2, 3, 4  --> new_list = [2, 4, 6, 8]
double = [(r * 2) for r in range(1, 5)]
print(double)

#Create a list of names having minimum length <CONDITIONAL>
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

#Create a list (refer above names) to capitalize those names which have maximum len
block_names = [n.upper() for n in names if len(n) > 5]
print(block_names)


