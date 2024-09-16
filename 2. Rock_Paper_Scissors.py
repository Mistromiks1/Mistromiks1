#Imported modules for random to generate random choices and for OS and Sys to end the code if a wrong number is chosen.
import random
import os
import sys

#Graphics for the rock, paper and scissors.
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

#Gets input from the user and prints the user choice or ends the programme is the choice is an invalid number.
rock_paper_scissors = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"You're chose: {rock_paper_scissors}")
if rock_paper_scissors == 0:
    print("rock")
    print(rock)
elif rock_paper_scissors == 1:
    print("paper")
    print(paper)
elif rock_paper_scissors == 2:
    print("scissors")
    print(scissors)
else:
    print("Please choose either 0, 1 or 2")
    os.execl(sys.executable, sys.executable, *sys.argv)

#Randomly generated choice by the computer.
computer_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_options)
print("Computer Chose:")
if computer_choice == "rock":
    print("rock")
    print (rock)
elif computer_choice == "paper":
    print("paper")
    print(paper)
else:
    print("scissors")
    print(scissors)

#The outcome of the choices.
if rock_paper_scissors == 0 and computer_choice == "rock":
    print("It's a draw")
if rock_paper_scissors == 1 and computer_choice == "paper":
    print("It's a draw")
if rock_paper_scissors == 2 and computer_choice == "scissors":
    print("It's a draw")
if rock_paper_scissors == 0 and computer_choice == "scissors":
    print("YOU WIN!!")
if rock_paper_scissors == 1 and computer_choice == "rock":
    print("YOU WIN!!")
if rock_paper_scissors == 2 and computer_choice == "paper":
    print("YOU WIN!!")
if rock_paper_scissors == 0 and computer_choice == "paper":
    print("You Lose")
if rock_paper_scissors == 1 and computer_choice == "scissors":
    print("You Lose")
if rock_paper_scissors == 2 and computer_choice == "rock":
    print("You Lose")