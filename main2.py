import random

option = ["rock", "paper", "scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ")
com_choice = random.choice(option)

print("You chose:", user_choice)
print("Computer chose:", com_choice)

if user_choice == com_choice:
    print("It's a tie!")
elif user_choice == "Rock" and com_choice == "Scissors":
    print("You win! Rock crushes Scissors.")
elif user_choice == "Paper" and com_choice == "Rock":
    print("You win! Paper covers Rock.")
elif user_choice == "Scissors" and com_choice == "Paper":
    print("You win! Scissors cut Paper.")
else:
    print("You lose! Better luck next time.")
# This code implements a simple Rock, Paper, Scissors game where the user plays against the computer.