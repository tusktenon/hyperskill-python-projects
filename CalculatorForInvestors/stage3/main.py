from textwrap import dedent

from calculator import Calculator


class App:
    def __init__(self, calculator):
        self.calculator = calculator
        print('Welcome to the Investor Program!')
        self.main_menu()

    def main_menu(self):
        while True:
            print(
                dedent("""\n\
                MAIN MENU
                0 Exit
                1 CRUD operations
                2 Show top ten companies by criteria
            """)
            )
            match input('Enter an option: '):
                case '0':
                    print('Have a nice day!')
                    return
                case '1':
                    self.crud_menu()
                case '2':
                    self.top_ten_menu()
                case _:
                    print('Invalid option!')

    def crud_menu(self):
        print(
            dedent("""\n\
            CRUD MENU
            0 Back
            1 Create a company
            2 Read a company
            3 Update a company
            4 Delete a company
            5 List all companies
        """)
        )
        match input('Enter an option: '):
            case '0':
                return
            case '1':
                self.create_company()
            case '2':
                self.read_company()
            case '3':
                self.update_company()
            case '4':
                self.delete_company()
            case '5':
                self.list_companies()
            case _:
                print('Invalid option!')

    def top_ten_menu(self):
        print(
            dedent("""\n\
            TOP TEN MENU
            0 Back
            1 List by ND/EBITDA
            2 List by ROE
            3 List by ROA
        """)
        )
        match input('Enter an option: '):
            case '0':
                return
            case '1' | '2' | '3':
                print('Not implemented!')
            case _:
                print('Invalid option!')

    def _lookup_company(self):
        name = input('Enter company name: ')
        if results := self.calculator.find_company_by_name(name):
            for i in range(len(results)):
                print(i, results[i][1])
            selection = int(input('Enter company number: '))
            return results[selection]
        else:
            print('Company not found!')
            return None

    def create_company(self):
        ticker = input("Enter ticker (in the format 'MOON'): ")
        name = input("Enter company (in the format 'Moon Corp'): ")
        sector = input("Enter industries (in the format 'Technology'): ")
        ebitda = input("Enter ebitda (in the format '987654321'): ")
        sales = input("Enter sales (in the format '987654321'): ")
        net_profit = input("Enter net profit (in the format '987654321'): ")
        market_price = input("Enter market price (in the format '987654321'): ")
        net_debt = input("Enter net debt (in the format '987654321'): ")
        assets = input("Enter assets (in the format '987654321'): ")
        equity = input("Enter equity (in the format '987654321'): ")
        cash_equivalents = input("Enter cash equivalents (in the format '987654321'): ")
        liabilities = input("Enter liabilities (in the format '987654321'): ")
        self.calculator.create_company(
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
        )
        print('Company created successfully!')

    def read_company(self):
        if company := self._lookup_company():
            print(company[0], company[1])
            for indicator, value in self.calculator.indicators(company[0]).items():
                print(f'{indicator} = {round(value, 2) if value else None}')

    def update_company(self):
        if company := self._lookup_company():
            ebitda = input("Enter ebitda (in the format '987654321'): ")
            sales = input("Enter sales (in the format '987654321'): ")
            net_profit = input("Enter net profit (in the format '987654321'): ")
            market_price = input("Enter market price (in the format '987654321'): ")
            net_debt = input("Enter net debt (in the format '987654321'): ")
            assets = input("Enter assets (in the format '987654321'): ")
            equity = input("Enter equity (in the format '987654321'): ")
            cash_equivalents = input("Enter cash equivalents (in the format '987654321'): ")
            liabilities = input("Enter liabilities (in the format '987654321'): ")
            self.calculator.update_company(
                company[0],
                ebitda,
                sales,
                net_profit,
                market_price,
                net_debt,
                assets,
                equity,
                cash_equivalents,
                liabilities,
            )
            print('Company updated successfully!')

    def delete_company(self):
        if company := self._lookup_company():
            self.calculator.delete_company(company[0])
            print('Company deleted successfully!')

    def list_companies(self):
        print('COMPANY LIST')
        for company in self.calculator.list_companies():
            print(*company)

def main():
    App(Calculator('investor.db', 'test/companies.csv', 'test/financial.csv'))


if __name__ == '__main__':
    main()
