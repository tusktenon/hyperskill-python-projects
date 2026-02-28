from collections import namedtuple
from random import randint

Account = namedtuple('Account', ['number', 'pin'])

accounts = []


def create_account():
    while True:
        number = 4000_0000_0000_0000 + 10 * randint(0, 999_999_999)
        if all(number != account.number for account in accounts):
            break
    pin = str(randint(0, 9999)).zfill(4)
    accounts.append(Account(number, pin))
    print('\nYour card has been created')
    print('Your card number:', number, sep='\n')
    print('Your card PIN:', pin, sep='\n')


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
