#Project 3 - Treasure Island
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
decs1 = input("\t Type \"left\" or \"right\" \n")

if decs1 == "left" or decs1 == "Left":
    print("You' ve come to a lake. There is an island in the middle of the lake.")
    decs2 = input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across\n")

    if decs2 == "wait" or decs2 == "Wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        decs3 = input("\tOne red, one yellow and one blue. Which colour do you choose?\n")

        if decs3 == "red" or decs3 == "Red":
            print("Burned by fire. Game Over.")
        elif decs3 == "yellow" or decs3 == "Yellow":
            print("You Win the Treasure Chest!!")
        elif decs3 == "blue" or decs3 == "Blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")
