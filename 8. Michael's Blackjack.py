import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#Cards and results to be printed
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

results = {
    "draw": "Draw 🙃",
    "you win": "You win 😁",
    "you lose": "You lose 😤",
    "user went over": "You went over. You lose 😒",
    "comp went over": "Opponent went over. You win 😌",
    "user blackjack": "BLACKJACK!! 🤩🥳",
    "comp blackjack": "Opponent has blackjack! You lose 😒"
}

#Defining the blackjack function.
def blackjack_project():
    """This function will run the Blackjack game."""
    print(logo)

    #Empty lists created to store the randomly generated cards for the user and computer.
    #Comp sum generated to spin the while loop later that randomly generates cards for the computer if comp score < 17.
    user_cards = []
    comp_cards = []
    comp_sum = sum(comp_cards)

    #Generating first two cards and initial score for the user
    for numb in (0, 2):
        rand_card = random.choice(cards)
        user_cards.append(rand_card)
    user_sum = sum(user_cards)
    print (f"    Your cards: {user_cards}, current score: {user_sum}")

    #Generating computer's first card and requesting if user wants to get another or pass.
    rand_comp_card = random.choice(cards)
    comp_cards.append(rand_comp_card)
    print(f"    Computer's first card: {rand_comp_card}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    #While loop to allow user to continue to choose cards until 21 is achieved or passed.
    while another_card == "y" and user_sum < 21:
        rand_card = random.choice(cards)
        user_cards.append(rand_card)
        user_sum = sum(user_cards)
        print(f"    Your cards: {user_cards}, current score: {user_sum}")

        #allows user to continue to request cards if sum < 21
        if user_sum < 21:
            print(f"    Computer's first card: {rand_comp_card}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        #Changes Ace from 11 to 1 IF an ace was in the user's hand and the user total goes over 21
        elif user_sum > 21 and cards[0] in user_cards:
            cards[0] = 1
            for num in range(len(user_cards)):
                if user_cards[num] == 11:
                    user_cards[num] = 1

    #If user achieves Blackjack, prints second card for the computer and prints results.
    if user_sum == 21:
        rand_comp_card = random.choice(cards)
        comp_cards.append(rand_comp_card)
        comp_sum = sum(comp_cards)
        print(f"    Your final hand: {user_cards}, final score: {user_sum}")
        print(f"    Computer's hand: {comp_cards}, final score: {comp_sum}")

    #if user is safe and chooses not to have any more cards, prints remaining cards for computer and final scores.
    elif another_card == 'n':
        print(f"    Your final hand: {user_cards}, final score: {user_sum}")
        while comp_sum < 17:

            rand_comp_card = random.choice(cards)
            comp_cards.append(rand_comp_card)
            comp_sum = sum(comp_cards)
        print(f"    Computer's final hand: {comp_cards}, final score: {comp_sum}")

    #Results to be printed at the end of the round.
    if user_sum == 21 and comp_sum != 21:
        print(results["user blackjack"])
    elif user_sum == 21 and comp_sum == 21:
        print(results["comp blackjack"])
    elif user_sum > comp_sum and user_sum<= 21 and comp_sum <= 21:
        print(results["you win"])
    elif user_sum < comp_sum and user_sum<= 21 and comp_sum <=21:
        print(results["you lose"])
    elif user_sum == comp_sum and user_sum<= 21 and comp_sum <=21:
        print(results["draw"])
    elif user_sum <= 21 and comp_sum > 21:
        print(results["comp went over"])
    elif user_sum > 21:
        print(results["user went over"])

    #If the user wishes to restart the function will be called again from the start.
    blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if blackjack == "y":
        blackjack_project()

#calling the function
blackjack_project()
