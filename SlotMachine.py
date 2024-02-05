# Caleb Kim
# 12/21/23
# This project simulates the functionality and experience of a slot machine.

import random

MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {

    "*": 4,
    "+": 6,
    "#": 2,
    "-": 3
}

winnings_chart = {

    "*": 4,
    "+": 2,
    "#": 0,
    "-": 1
}


def initial_deposit():
    while True:

        amount = input("How much would you like to deposit? (Numerical values only please) $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break

            else:
                print(f"Input must be greater than ${0}. Please try again.")

        else:
            print("Invalid request. Please try again.")

    return amount


def deposit(balance):
    while True:
        amount = input("How much would you like to deposit? (Numerical values only please) $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                balance += amount
                break

            else:
                print(f"Input must be greater than ${0}. Please try again.")

        else:
            print("Invalid request. Please try again.")

    return balance


def get_lines():
    while True:

        lines = input("Please enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ") ")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break

            else:
                print(f"Input must be between {1} and {MAX_LINES}. Please try again.")

        else:
            print("Invalid request. Please try again.")

    return lines


def get_bet():
    while True:

        amount = input("How much would you like to bet? (Numerical values only please) $")

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount:
                break

            else:
                print(f"Input must be greater than or equal to ${1}. Please try again.")

        else:
            print("Invalid request. Please try again.")

    return amount


def hub(balance):
    while True:
        ui = input(
            "\nThank you for using STAR SLOT MACHINE.\nHere is our current list of options.\nPress 0 to exit.\nPress 1 to make an additional deposit.\nPress 2 to place a bet and spin the slot machine.\nPress 3 to look at your current balance inside of the slot machine.\n->")

        if ui.isdigit():
            ui = int(ui)
            if ui == 0:
                print(
                    f"You have exited the game with ${balance}.\nPlease do not forget to collect your earnings and we hope to see you again soon.")
                break
            if ui == 1:
                balance = deposit(balance)
            if ui == 2:
                balance = process(balance)
            if ui == 3:
                print(f"${balance}")


def process(balance):
    while True:

        curr_lines = get_lines()
        curr_bet = get_bet()

        if curr_bet <= balance:
            total_bet = curr_bet * curr_lines

            if total_bet <= balance:

                curr_balance = balance - total_bet
                print(
                    f"\nYou are betting ${curr_bet} on {curr_lines} line(s). \nYour total bet is currently: ${total_bet}.\nYour current balance is now ${curr_balance}.")
                slots = get_spin(ROWS, COLS, symbol_count)
                spin(slots)
                curr_balance = check_winnings(slots, curr_lines, curr_bet, winnings_chart, curr_balance)
                return curr_balance

            else:
                print(
                    "Inputted bet amount of greater than current balance in account.\nPlease deposit more money into the machine or lower the bet amount.")
                break

        else:
            print(
                "Inputted bet amount of greater than current balance in account.\nPlease deposit more money into the machine or lower the bet amount.")
            break

    return balance


def get_spin(r, c, s):
    all_symbols = []
    for symbol, symbol_count in s.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(c):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(r):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def spin(columns):
    ui = input("Please enter any key when you are ready to spin.")
    if ui.isprintable():
        print_slot(columns)


def check_winnings(columns, lines, bet, values, curr_balance):
    winnings = 0
    winning_lines = []
    won = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            curr_balance += winnings
            win = True
            print(f"Congratulations, you have won ${winnings} from line {line + 1}")

    if winnings == 0:
        print(f"\nUnfortunately, you haven't won anything.")
    print(f"Your updated balance is now ${curr_balance}.")
    return curr_balance


def print_slot(columns):
    print("\nSTAR SLOT MACHINE:\n")

    for row in range(len(columns[0])):
        print("{ ", end="")
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" }")
        print()


def main():
    balance = initial_deposit()
    hub(balance)


main()
