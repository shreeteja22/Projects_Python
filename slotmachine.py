import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:  # Only runs if the loop wasn't broken
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin_of_slot(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Enter the deposit amount (in $): ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The number should be greater than zero.")
        else:
            print("The input should be an integer.")
    return amount


def no_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("The input should be an integer.")
    return lines


def betting():
    while True:
        amount = input(f"Enter the amount you want to bet per line (in $): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("The input should be an integer.")
    return amount


def spin(balance):
    lines = no_of_lines()
    while True:
        bet = betting()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet. Your total bet is ${total_bet}, but your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    slots = spin_of_slot(ROWS, COLS, symbol_count)
    print_slot(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}!")
    
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play or 'q' to quit: ")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
