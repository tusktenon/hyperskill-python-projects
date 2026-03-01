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

    @staticmethod
    def is_valid_number(n):
        return CardUtils.luhn_sum(n) % 10 == 0


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

    def lookup(self, number, pin=None):
        if pin is None:
            self.cur.execute('SELECT id FROM card WHERE number = ?', (number,))
        else:
            self.cur.execute('SELECT id FROM card WHERE number = ? AND pin = ?', (number, pin))
        res = self.cur.fetchone()
        return res[0] if res else None

    def get_balance(self, id):
        return self.cur.execute('SELECT balance FROM card WHERE id = ?', (id,)).fetchone()[0]

    def deposit(self, id, amount):
        self.cur.execute('UPDATE card SET balance = balance + ? WHERE id = ?', (amount, id))
        self.conn.commit()

    def transfer(self, src_id, dest_id, amount):
        if self.get_balance(src_id) < amount:
            raise ValueError('Not enough money!')
        sql = 'UPDATE card SET balance = balance + ? WHERE id = ?'
        self.cur.execute(sql, (-amount, src_id))
        self.cur.execute(sql, (amount, dest_id))
        self.conn.commit()

    def close_account(self, id):
        self.cur.execute('DELETE FROM card WHERE id = ?', (id,))
        self.conn.commit()


class App:
    def __init__(self, accounts):
        self.accounts = accounts

    def main_menu(self):
        while True:
            print('\n1. Create an account\n2. Log into account\n0. Exit')
            match input():
                case '0':
                    print('\nBye!')
                    return
                case '1':
                    self.create_account()
                case '2':
                    self.login()

    def logged_in_menu(self, id):
        while True:
            print(
                '\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit'
            )
            match input():
                case '1':
                    print(f'\nBalance: {self.accounts.get_balance(id)}')
                case '2':
                    amount = int(input('\nEnter income: '))
                    self.accounts.deposit(id, amount)
                    print('Income was added!')
                case '3':
                    self.transfer(id)
                case '4':
                    self.accounts.close_account(id)
                    print('\nThe account has been closed!')
                    return
                case '5':
                    print('\nYou have successfully logged out!')
                    return
                case '0':
                    print('\nBye!')
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

    def transfer(self, src_id):
        print('\nTransfer')
        dest_card = input('Enter card number: ')
        if not CardUtils.is_valid_number(dest_card):
            print('Probably you made a mistake in the card number. Please try again!')
            return
        dest_id = self.accounts.lookup(dest_card)
        if dest_id is None:
            print('Such a card does not exist.')
            return
        if dest_id == src_id:
            print("You can't transfer money to the same account!")
            return
        amount = int(input('Enter how much money you want to transfer: '))
        try:
            self.accounts.transfer(src_id, dest_id, amount)
        except ValueError as err:
            print(err)
        else:
            print('Success!')


App(Accounts('card.s3db')).main_menu()
