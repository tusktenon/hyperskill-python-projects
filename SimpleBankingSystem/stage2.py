from collections import namedtuple
from random import randint

Account = namedtuple('Account', ['number', 'pin'])

accounts = []


def create_account():
    while True:
        number = 4000_0000_0000_000 + randint(0, 99_9999_999)
        if all(number != account.number // 10 for account in accounts):
            break
    number = 10 * number + luhn_check_digit(number)
    pin = str(randint(0, 9999)).zfill(4)
    accounts.append(Account(number, pin))
    print('\nYour card has been created')
    print('Your card number:', number, sep='\n')
    print('Your card PIN:', pin, sep='\n')


def luhn_check_digit(n):
    digits = list(map(int, str(n)))
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    luhn_sum = sum(digits)
    return 10 * ((luhn_sum + 9) // 10) - luhn_sum


def login():
    number = int(input('\nEnter your card number: '))
    pin = input('Enter your PIN: ')
    if (number, pin) in accounts:
        print('\nYou have successfully logged in!')
        logged_in_menu()
    else:
        print('\nWrong card number or PIN!')


def logged_in_menu():
    while True:
        print('\n1. Balance\n2. Log out\n0. Exit')
        match input():
            case '1':
                print('\nBalance: 0')
            case '2':
                print('\nYou have successfully logged out!')
                return
            case '0':
                exit(0)


def main_menu():
    while True:
        print('\n1. Create an account\n2. Log into account\n0. Exit')
        match input():
            case '0':
                return
            case '1':
                create_account()
            case '2':
                login()


main_menu()
