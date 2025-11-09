import random

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
comp_Number = random.randint(1, 101)
print(f"Pssst, the correct answer is {comp_Number}")

difficulty =  input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess_at_last_moment():
    global guess #using namespace
    print(f"You have 1 attempt remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == comp_Number:
        print(f"You got it! The answer was {comp_Number}")
    else:
        print("You've run out of guesses. Refresh the page to run again.")

if difficulty == 'easy':
    attempt = 10
    while attempt >= 2:
            print(f"You have {attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < comp_Number:
                print("Too Low.")
                print("Guess Again.")
            elif guess > comp_Number:
                print("Too high.")
                print("Guess Again.")
            else:
                print(f"You got it! The answer was {comp_Number}")
                break
            attempt -= 1

    if attempt == 1:
        guess_at_last_moment()

elif difficulty == 'hard':
    attempt = 5
    while attempt >= 2:
            print(f"You have {attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < comp_Number:
                print("Too Low.")
                print("Guess Again.")
            elif guess > comp_Number:
                print("Too high.")
                print("Guess Again.")
            else:
                print(f"You got it! The answer was {comp_Number}")
                break
            attempt -= 1

    if attempt == 1:
        guess_at_last_moment()