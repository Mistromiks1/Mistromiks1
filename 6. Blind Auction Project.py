logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

#empty dictionary to store bidders.
blind_auction = {}
additional_bidders = "yes"

#while loop to keep adding bidders
while additional_bidders == "yes":
    user = input("What is your name?:")
    bid = int(input("What is your bid?: $"))

    blind_auction[user] = bid
    additional_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    #prints spaces to stop bidders from seeing the bids of other bidders
    if additional_bidders == "yes":
        print("\n" * 100)
    else:
        print("\n")

#function to calculate the highest bidder in the dictionary
def find_highest_bidder():
    winner = ""
    highest_bid = 0
    for key in blind_auction:
        bid_amount = blind_auction[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"{winner} is the highest bidder with ${highest_bid}")

find_highest_bidder()