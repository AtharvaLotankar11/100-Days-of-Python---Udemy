from prettytable import PrettyTable

#Create an object 'table'
table = PrettyTable()

#Create a pokemon table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Align to left
table.align = "l"
print(table)
