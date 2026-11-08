

# Made by Salman
import random

print("==============================")
print("--- Rock Paper Scissors ---")
print("==============================")
print("play against the computer!")

choices = ["rock", "paper", "scissors"]


user_score = 0
computer_score = 0

while True:
    user = input("\nWhat are you choice? /rock / paper / scissors (chooice the q for quit): ").lower()

    if user == "q":
        print("\n--- Final Score ---")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("End the Game! Bye Bye!")
        break

    if user not in choices:
        print("wrong choice! Plz Try again !")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win! 🎉")
        user_score = user_score + 1
    else:
        print("Computer Wins! 😢")
        computer_score = computer_score + 1

    
    print(f"Score -> You: {user_score} | Computer: {computer_score}")
