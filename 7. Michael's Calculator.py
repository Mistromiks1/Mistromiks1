logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4,8))

run_programme = "y"

cont_or_new = ""
while run_programme == "y":

    if cont_or_new == "" or cont_or_new == "n":
        print(logo)
        first_num = float(input("What is the first number?: "))

        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_num = float(input("What is the next number?: "))
    else:

        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_num = float(input("What is the next number?: "))

    output = operations[operation](first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {output}")

    cont_or_new = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation or type 'e' to end:").lower()

    if cont_or_new == "y":
        first_num = output
    if cont_or_new == "n":
        print("\n" * 100)
    if cont_or_new == "e":
        run_programme = "e"