MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter the number of amount..(in $) : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The number should be greater than zero")
        else:
            print("The input should be integer")
    return amount

def no_of_lines():
    while True:
        lines = input("Enter the number of lines..(between 1-",+ str(MAX_LINES)+ ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number should be in between 1-3")
        else:
            print("The input should be integer")
    return lines


def betting():
    while True:
        amount = input("Enter the number of amount you want to bet..(in $) : ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # print("The number should be in between " + str(MIN_BET) + " - " + str(MIN_BET))
                print(f"The number should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("The input should be integer")
    return amount
    

def main():
    balance = deposit()
    lines = no_of_lines()
    while True:
        bet = betting()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough balance to bet.Your bet total is ${total_bet} & your balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines}.Total bet is ${total_bet}")
    print(balance,lines)