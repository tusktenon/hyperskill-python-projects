import sqlite3
from random import randint


class CardUtils:
    @staticmethod
    def generate_card_number():
        number = str(4000_0000_0000_000 + randint(0, 99_9999_999))
        return number + CardUtils.luhn_check_digit(number)

    @staticmethod
    def generate_pin():
        return str(randint(0, 9999)).zfill(4)

    @staticmethod
    def luhn_sum(n):
        digits = list(map(int, n))
        for i in range(0, len(digits), 2):
            d = digits[i]
            digits[i] = 2 * d if d < 5 else 2 * d - 9
        return sum(digits)

    @staticmethod
    def luhn_check_digit(n):
        return str((10 - CardUtils.luhn_sum(n) % 10) % 10)


class Accounts:
    def __init__(self, datafile):
        self.conn = sqlite3.connect(datafile)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def create_account(self):
        while True:
            number = CardUtils.generate_card_number()
            pin = CardUtils.generate_pin()
            res = self.cur.execute('SELECT id FROM card WHERE number = ?', (number,))
            if not res.fetchone():
                break
        self.cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (number, pin))
        self.conn.commit()
        return number, pin

    def lookup(self, number, pin):
        self.cur.execute('SELECT id FROM card WHERE number = ? AND pin = ?', (number, pin))
        res = self.cur.fetchone()
        return res[0] if res else None

    def get_balance(self, id):
        return self.cur.execute('SELECT balance FROM card WHERE id = ?', (id,)).fetchone()[0]


class App:
    def __init__(self, accounts):
        self.accounts = accounts

    def main_menu(self):
        while True:
            print('\n1. Create an account\n2. Log into account\n0. Exit')
            match input():
                case '0':
                    return
                case '1':
                    self.create_account()
                case '2':
                    self.login()

    def logged_in_menu(self, id):
        while True:
            print('\n1. Balance\n2. Log out\n0. Exit')
            match input():
                case '1':
                    print(f'\nBalance: {self.accounts.get_balance(id)}')
                case '2':
                    print('\nYou have successfully logged out!')
                    return
                case '0':
                    exit(0)

    def create_account(self):
        number, pin = self.accounts.create_account()
        print('\nYour card has been created')
        print('Your card number:', number, sep='\n')
        print('Your card PIN:', pin, sep='\n')

    def login(self):
        number = int(input('\nEnter your card number: '))
        pin = input('Enter your PIN: ')
        if id := self.accounts.lookup(number, pin):
            print('\nYou have successfully logged in!')
            self.logged_in_menu(id)
        else:
            print('\nWrong card number or PIN!')


App(Accounts('card.s3db')).main_menu()
