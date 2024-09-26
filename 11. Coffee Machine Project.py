MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def print_resources():
    """Prints a list of the remaining resources"""
    print (f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money_collected}")

def resource_check(water_needed, milk_needed, coffee_needed):
    """Checks available resources to determine if enough resources are there to produce the drink"""
    if water_needed > resources["water"]:
        return "Sorry there is not enough water."
    elif milk_needed > resources["milk"]:
        return "Sorry there is not enough milk."
    elif coffee_needed > resources["coffee"]:
        return "Sorry there is not enough coffee."
    else:
        return "Please insert coins."

def coins_paid():
    """This function prompts user to input the coins they will pay and calculates the total cash given and returns
    the total."""
    quarters_paid = int(input("how many quarters?: "))
    dimes_paid = int(input("how many dimes?: "))
    nickles_paid = int(input("how many nickles?: "))
    pennies_paid = int(input("how many pennies?: "))

    total_paid = (quarters_paid * 0.25) + (dimes_paid * 0.10) + (nickles_paid * 0.05) + (pennies_paid * 0.01)

    return total_paid

def cash_check(cash_paid, item_cost):
    """This function compares the coins paid and the price of the item and returns the amount of change"""
    if cash_paid >= item_cost:
        change_due = cash_paid - item_cost
        exact_change = round(change_due, 2)
        print(f"Here is ${exact_change} in change.")
        return exact_change
    else:
        extra_needed = item_cost - cash_paid
        exact_extra_needed = round(extra_needed, 2)
        print (f"Sorry that's not enough money. You need ${exact_extra_needed} more. Money refunded")
        return -exact_extra_needed

def reduce_resources(reduce_water, reduce_milk, reduce_coffee):
    """Reduces amount of each resource by the amount needed to produce the coffee product."""
    resources["water"] -= reduce_water
    resources["milk"] -= reduce_milk
    resources["coffee"] -= reduce_coffee

money_collected = 0
def profit_tally(drink_cost):
    """Everytime a drink is bought, this code adds the price of the drink to the cash total."""
    global money_collected
    money_collected += drink_cost


#Loop that allows the user to choose and pay for a drink until the machine is turned off.
machine_state = "on"
while machine_state == "on":
    user_request = input("What would you like? (espresso, latte, cappuccino): ").lower()

    #prints the report of resources left and money collected
    if user_request == "report":
        print_resources()

    #Checks if enough resources are available, takes the cash, returns the change or requests more money.
    elif user_request == "espresso":
        available = resource_check(50, 0, 18)
        if available == "Please insert coins.":
            print(f"Please insert coins.\nThe cost is ${MENU["espresso"]["cost"]}")
            change = cash_check(coins_paid(), MENU["espresso"]["cost"])

            #if enough money is given, gives espresso, reduces resources available and adds the cost to the cash tally.
            if change >= 0:
                print("Here is your espresso ☕. Enjoy!")
                reduce_resources(50, 0, 18)
                profit_tally(MENU["espresso"]["cost"])

        #Prints which resource is unavailable
        else:
            print(available)

    elif user_request == "latte":
        available = resource_check(200, 150, 24)
        if available == "Please insert coins.":
            print(f"Please insert coins.\nThe cost is ${MENU["latte"]["cost"]}")
            change = cash_check(coins_paid(), MENU["latte"]["cost"])
            if change >=0:
                print("Here is your latte ☕. Enjoy!")
                reduce_resources(200, 150,24)
                profit_tally(MENU["latte"]["cost"])
        else:
            print(available)

    elif user_request == "cappuccino":
        available = resource_check(250, 100, 24)
        if available == "Please insert coins.":
            print(f"Please insert coins.\nThe cost is ${MENU["cappuccino"]["cost"]}")
            change = cash_check(coins_paid(), MENU["cappuccino"]["cost"])
            if change >= 0:
                print("Here is your cappuccino ☕. Enjoy!")
                reduce_resources(250, 100, 24)
                profit_tally(MENU["cappuccino"]["cost"])
        else:
            print(available)

    #Turns off the machine and ends the loop.
    elif user_request == "off":
        machine_state = user_request
