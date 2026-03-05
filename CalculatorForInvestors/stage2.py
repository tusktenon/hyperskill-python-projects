import csv
import sqlite3


class Calculator:
    def __init__(self, database_file, companies_file, financial_file):
        self.con = sqlite3.connect(database_file)
        self.cur = self.con.cursor()
        self._create_companies_table()
        self._import_company_data(companies_file)
        self._create_financial_table()
        self._import_financial_data(financial_file)

    def _create_companies_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS companies(
            ticker TEXT PRIMARY KEY,
            name TEXT,
            sector TEXT)""")
        self.con.commit()

    def _import_company_data(self, companies_file):
        with open(companies_file, newline='') as src_file:
            company_reader = csv.reader(src_file, delimiter=',')
            header_row = True
            for line in company_reader:
                if not header_row:
                    self.cur.execute('INSERT INTO companies VALUES (?, ?, ?)', tuple(line))
                header_row = False
        self.con.commit()

    def _create_financial_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS financial(
            ticker TEXT PRIMARY KEY,
            ebitda REAL,
            sales REAL,
            net_profit REAL,
            market_price REAL,
            net_debt REAL,
            assets REAL,
            equity REAL,
            cash_equivalents REAL,
            liabilities REAL)""")
        self.con.commit()

    def _import_financial_data(self, financial_file):
        with open(financial_file, newline='') as src_file:
            financial_reader = csv.reader(src_file, delimiter=',')
            header_row = True
            for line in financial_reader:
                if not header_row:
                    entry = (line[0], *map(lambda x: float(x) if x else None, line[1:]))
                    self.cur.execute(
                        'INSERT INTO financial VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entry
                    )
                header_row = False
        self.con.commit()


Calculator('investor.db', 'test/companies.csv', 'test/financial.csv')
print('Database created successfully!')
