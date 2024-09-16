# Importing the random module. Graphic art for the intro, stages, and word list
import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fruit = ["apple", "banana", "mango", "orange", "grape", "papaya", "pineapple", "blueberry", "kiwi", "watermelon"]
sport = ["soccer", "basketball", "tennis", "baseball", "cricket", "swimming", "hockey", "volleyball", "badminton", "rugby"]
vegetable = ["carrot", "broccoli", "spinach", "cucumber", "lettuce", "zucchini", "cauliflower", "asparagus", "tomato", "eggplant"]
emotion = ["happy", "sad", "angry", "excited", "nervous", "frustrated", "surprised", "scared", "confident", "lonely"]
food = ["pizza", "sushi", "burger", "pasta", "sandwich", "tacos", "lasagna", "omelette", "pancakes", "salad"]
country = ["canada", "brazil", "australia", "japan", "germany", "egypt", "argentina", "italy", "india", "mexico"]
city = ["paris", "tokyo", "london", "rome", "new delhi", "moscow", "washington", "madrid", "beijing", "berlin"]
animal = ["elephant", "dolphin", "kangaroo", "giraffe", "tiger", "penguin", "zebra", "lion", "gorilla", "koala"]

word_list = [fruit, vegetable, emotion, sport, food, country, city, animal]
word_list_str = ["fruit", "vegetable", "emotion", "sport", "food", "country", "city", "animal"]

#Choosing random word from lists. Printing the logo and the initial blanks spaces to show letters to be filled.
list_name = random.randint(0, 7)
word_number = random.randint(0, 9)

chosen_word = word_list[list_name][word_number]

print(logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

#Print the category of word.
word_category = word_list_str[list_name]
print(f"The word is a {word_category}")


#Assigning number of lives, empty string to house updated word and creating lists to house the guessed letters.
lives = 6

display = ""
previously_guessed = []
incorrect_letters = []

#While loop to allow user to keep guessing letters
while chosen_word != display and lives > 0:
    print(f"Lives left: {lives}")
    print(f"Incorrect letters previously guessed: {incorrect_letters}")
    guess = input("Guess a letter: \n").lower()

    #Lets user know they have guessed that letter already.
    if guess in previously_guessed:
        print(f"You've already guessed: {guess}")
    if guess in incorrect_letters:
        print(f"You've already guessed {guess} and it is NOT a part of the word.")

    #prints the updated word with each additional guess. Includes previously guessed letters.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            previously_guessed += letter
        elif letter in previously_guessed:
            display += letter
        else:
            display += "_"

    print(display)

    #Incorrect guesses reduce lives til zero, allows user to know they have lost and ends while loop.
    if guess not in chosen_word:
        lives -= 1
        incorrect_letters += guess
        print(f"{guess} is not in the word")
        if lives == 1:
            print("Careful, 1 life remaining")
        elif lives == 0:
            print("*******************YOU LOSE*******************")
            print(f"The word was: {chosen_word}")

    print(stages[lives])

    #resets the display word if incomplete so it won't keep adding the entire string to previous strings.
    #Ends the while loop if word is completed.
    if display != chosen_word:
        display = ""
    else:
        print("*******************YOU WIN!*******************")

    #adds spaces between subsequent guesses.
    print("\n\n")
