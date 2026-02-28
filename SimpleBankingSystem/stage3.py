import sqlite3
from random import randint

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    )
""")


def create_account():
    number = generate_card_number()
    pin = str(randint(0, 9999)).zfill(4)
    cur.execute(f'INSERT INTO card (number, pin) VALUES ({number}, {pin})')
    conn.commit()
    print('\nYour card has been created')
    print('Your card number:', number, sep='\n')
    print('Your card PIN:', pin, sep='\n')


def generate_card_number():
    while True:
        number = 4000_0000_0000_000 + randint(0, 99_9999_999)
        number = 10 * number + luhn_check_digit(number)
        number = str(number)
        res = cur.execute(f'SELECT id FROM card WHERE number = {number}')
        if not res.fetchone():
            return number


def luhn_check_digit(n):
    digits = list(map(int, str(n)))
    for i in range(0, len(digits), 2):
        d = digits[i]
        digits[i] = 2 * d if d < 5 else 2 * d - 9
    return (10 - sum(digits) % 10) % 10


def login():
    number = int(input('\nEnter your card number: '))
    pin = input('Enter your PIN: ')
    res = cur.execute(f'SELECT id FROM card WHERE number = {number} AND pin = {pin}').fetchone()
    if res:
        print('\nYou have successfully logged in!')
        logged_in_menu(res[0])
    else:
        print('\nWrong card number or PIN!')


def logged_in_menu(id):
    while True:
        print('\n1. Balance\n2. Log out\n0. Exit')
        match input():
            case '1':
                res = cur.execute(f'SELECT balance FROM card WHERE id = {id}')
                balance = res.fetchone()[0]
                print(f'\nBalance: {balance}')
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
