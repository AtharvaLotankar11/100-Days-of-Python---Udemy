states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[len(states_of_america) - 1]) #last element = len - 1 (Avoids IndexError)

#Synthesize two lists
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]
dirtyDozen = [fruits, veg]
print(dirtyDozen[1][1])

#(list[1][1] = 1st from original list: veg then again 1st in veg: Kale)
