#There is no block scope in Python

if 3 > 2:
    a_variable = 10

game_level = 3
enemies = ["Skeleton", "Zombies", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)