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
        self.cur.execute('SELECT ticker FROM companies')
        if self.cur.fetchone():
            return
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
        self.cur.execute('SELECT ticker FROM financial')
        if self.cur.fetchone():
            return
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

    def create_company(
        self,
        ticker,
        name,
        sector,
        ebitda,
        sales,
        net_profit,
        market_price,
        net_debt,
        assets,
        equity,
        cash_equivalents,
        liabilities,
    ):
        self.cur.execute('INSERT INTO companies VALUES (?, ?, ?)', (ticker, name, sector))
        self.cur.execute(
            'INSERT INTO financial VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (
                ticker,
                ebitda,
                sales,
                net_profit,
                market_price,
                net_debt,
                assets,
                equity,
                cash_equivalents,
                liabilities,
            ),
        )
        self.con.commit()

    def update_company(
        self,
        ticker,
        ebitda,
        sales,
        net_profit,
        market_price,
        net_debt,
        assets,
        equity,
        cash_equivalents,
        liabilities,
    ):
        self.cur.execute(
            """UPDATE financial
                SET ebitda = ?,
                    sales = ?,
                    net_profit = ?,
                    market_price = ?,
                    net_debt = ?,
                    assets = ?,
                    equity = ?,
                    cash_equivalents = ?,
                    liabilities = ?
                WHERE ticker = ?""",
            (
                ebitda,
                sales,
                net_profit,
                market_price,
                net_debt,
                assets,
                equity,
                cash_equivalents,
                liabilities,
                ticker,
            ),
        )
        self.con.commit()

    def delete_company(self, ticker):
        self.cur.execute('DELETE FROM companies WHERE ticker = ?', (ticker,))
        self.cur.execute('DELETE FROM financial WHERE ticker = ?', (ticker,))
        self.con.commit()

    def find_company_by_name(self, name):
        self.cur.execute('SELECT ticker, name FROM companies WHERE name LIKE ?', (f'%{name}%',))
        return self.cur.fetchall()

    def indicators(self, ticker):
        self.cur.execute(
            """SELECT ebitda, sales, net_profit, market_price, net_debt, assets, equity, liabilities
               FROM financial WHERE ticker = ?""",
            (ticker,),
        )
        ebitda, sales, net_profit, market_price, net_debt, assets, equity, liabilities = (
            self.cur.fetchone()
        )
        return {
            'P/E': _ratio_or_none(market_price, net_profit),
            'P/S': _ratio_or_none(market_price, sales),
            'P/B': _ratio_or_none(market_price, assets),
            'ND/EBITDA': _ratio_or_none(net_debt, ebitda),
            'ROE': _ratio_or_none(net_profit, equity),
            'ROA': _ratio_or_none(net_profit, assets),
            'L/A': _ratio_or_none(liabilities, assets),
        }

    def list_companies(self):
        self.cur.execute('SELECT * FROM companies ORDER BY ticker')
        return self.cur.fetchall()


def _ratio_or_none(a, b):
    return a / b if a and b else None
