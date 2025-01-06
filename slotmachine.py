import random

# Constants defining maximum and minimum values
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# A dictionary to store the count of each symbol
symbol_count = {
    "A": 2,  # Symbol A appears 2 times
    "B": 4,  # Symbol B appears 4 times
    "C": 6,  # Symbol C appears 6 times
    "D": 8   # Symbol D appears 8 times
}

# A dictionary to store the value of each symbol
symbol_values = {
    "A": 5,  # Symbol A has a value of 5
    "B": 4,  # Symbol B has a value of 4
    "C": 3,  # Symbol C has a value of 3
    "D": 2   # Symbol D has a value of 2
}

# Function to check the winnings based on the symbols in each column
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize winnings to zero
    winning_lines = []  # List to store the winning lines
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol in the first column of the line
        for column in columns:
            if column[line] != symbol:  # If any symbol in the column is different, break
                break
        else:  # Only runs if the loop wasn't broken (all symbols match)
            winnings += values[symbol] * bet  # Calculate winnings
            winning_lines.append(line + 1)  # Add the line number to winning lines

    return winnings, winning_lines  # Return total winnings and the winning lines


# Function to simulate the slot machine spin and return the columns with symbols
def spin_of_slot(rows, cols, symbols):
    all_symbols = []  # List to store all symbols
    for symbol, count in symbols.items():  # Loop through each symbol and its count
        for _ in range(count):
            all_symbols.append(symbol)  # Add each symbol according to its count

    columns = []  # List to store the columns of the slot machine
    for _ in range(cols):  # Loop to generate columns
        column = []  # List to store each column's symbols
        current_symbols = all_symbols[:]  # Create a copy of all symbols
        for _ in range(rows):  # Loop to fill the column with symbols
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove the selected symbol to avoid repetition
            column.append(value)  # Add the symbol to the column

        columns.append(column)  # Add the column to the columns list

    return columns  # Return the generated columns with symbols


# Function to print the slot machine columns in a readable format
def print_slot(columns):
    for row in range(len(columns[0])):  # Loop through each row of symbols
        for i, column in enumerate(columns):  # Loop through each column
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbols with separator
            else:
                print(column[row], end="")  # Print the last symbol without separator
        print()  # Move to the next line


# Function to ask for deposit amount
def deposit():
    while True:
        amount = input("Enter the deposit amount (in $): ")
        if amount.isdigit():  # Check if input is a valid number
            amount = int(amount)
            if amount > 0:
                break  # Exit loop if valid amount entered
            else:
                print("The number should be greater than zero.")
        else:
            print("The input should be an integer.")
    return amount  # Return the deposit amount


# Function to ask how many lines the player wants to bet on
def no_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break  # Exit loop if valid number of lines entered
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("The input should be an integer.")
    return lines  # Return the number of lines to bet on


# Function to ask for the betting amount per line
def betting():
    while True:
        amount = input(f"Enter the amount you want to bet per line (in $): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break  # Exit loop if valid bet amount entered
            else:
                print(f"Please enter a bet between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("The input should be an integer.")
    return amount  # Return the bet amount


# Main function to run the game
def spin(balance):
    lines = no_of_lines()  # Ask the player how many lines to bet on
    while True:
        bet = betting()  # Ask for the bet amount per line
        total_bet = bet * lines  # Calculate the total bet
        if total_bet > balance:  # Check if the player has enough balance
            print(f"You don't have enough balance to bet. Your total bet is ${total_bet}, but your balance is ${balance}.")
        else:
            break  # Exit loop if player has enough balance

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    slots = spin_of_slot(ROWS, COLS, symbol_count)  # Spin the slot machine
    print_slot(slots)  # Print the result of the spin

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)  # Check if the player won
    print(f"You won ${winnings}!")  # Display the winnings
    
    return winnings - total_bet  # Return the net result (winnings - bet)


# Main game loop
def main():
    balance = deposit()  # Ask for the initial deposit amount
    while True:
        print(f"Current balance is ${balance}")  # Display current balance
        answer = input("Press Enter to play or 'q' to quit: ")  # Ask if the player wants to continue or quit
        if answer.lower() == "q":
            break  # Exit loop if player chooses to quit
        balance += spin(balance)  # Spin the slot and update the balance

    print(f"You left with ${balance}")  # Display the final balance after quitting


main()  # Start the game
