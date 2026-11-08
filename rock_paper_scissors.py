# Made by Salman
import random
print("===============================")
print("--- Rock Paper Scissors ---")
print("===============================")
print("play against the computer!")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nWhat are you choice? /rock / paper / scissors (chooice the q for quit): ").lower()

    if user == "q":
        print("End the Game! Bye Bye!")
        break

    if user not in choices:
        print("wrong choice! Plz Try again !")
        continue

    computer = random.choice(choices)
    print(f"Computer choice is : {computer}")

    if user == computer:
        print("Draw ! Try again")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win! 🎉")
    else:
        print("Computer Win ! 😅")
