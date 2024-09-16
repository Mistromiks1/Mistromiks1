#importing the random module
import random

#list of all the usable characters for a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#printing instructions and getting inputs from the user
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#empty list to place the randomly chosen characters into
rng_characters = []

#based on the number of each item selected by the user, search through each master list and randomly populate new list
#multiplied by nr_letters etc so that there are always enough options to choose from.

for letter in letters * nr_letters:
    if nr_letters > 0:
        rng_characters.append(random.choice(letters))
        nr_letters -= 1

for symbol in symbols * nr_symbols:
    if nr_symbols > 0:
        rng_characters.append(random.choice(symbols))
        nr_symbols -= 1

for number in numbers * nr_numbers:
    if nr_numbers > 0:
        rng_characters.append(random.choice(numbers))
        nr_numbers -= 1

#empty string to store the first password draft into
password = ""

#printing the password draft into that string pulling each character from the list
for character in rng_characters:
    password += character
#print (password)

#scrambling the password list
random.shuffle(rng_characters)

#taking the characters from the list and putting them together into a string and printing it
scrambled_password = ""
for rnd_character in rng_characters:
    scrambled_password += rnd_character
print(f"Your password is: {scrambled_password}")
