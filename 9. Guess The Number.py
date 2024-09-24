logo = """
  /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
"""
import random

#Generate random number, print intro info and choose difficulty.
numb = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#Generate number of attempts based on difficulty chosen.
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5
else:
    print("You have made an incorrect choice")

#Defining function that takes guesses and compares it to number generated
def guess_the_number():
    """Function requests a guess and compares it to the randomly generated number"""
    global attempt
    for i in range (attempt):
        print (f" You have {attempt} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == numb:
            print(f"You got it! The answer is {numb} 😁😁")
            return
        elif guess > numb and attempt == 1:
            print("Too high.")
        elif guess < numb and attempt == 1:
            print("Too low.")
        elif guess > numb:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
        attempt -= 1
    print("You've run out of guesses, you lose.")
    return

#calling the function
guess_the_number()