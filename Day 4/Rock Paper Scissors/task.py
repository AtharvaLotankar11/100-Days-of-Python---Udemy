import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if option == 0:
    print(rock)
elif option == 1:
    print(paper)
elif option == 2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

if option == 0 or option == 1 or option == 2:
    print("Computer Chose:")
    rps = [rock, paper, scissors]
    compChoice = random.choice(rps)
    print(compChoice)

    if option == 0:
        if compChoice == rock:
            print("Draw!")
        elif compChoice == paper:
            print("You Lose")
        else:
            print("You Win")
    elif option == 1:
        if compChoice == rock:
            print("You Win")
        elif compChoice == paper:
            print("Draw!")
        else:
            print("You Lose")
    elif option == 2:
        if compChoice == rock:
            print("You Lose")
        elif compChoice == paper:
            print("You Win")
        else:
            print("Draw!")
