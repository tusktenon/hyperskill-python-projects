from textwrap import dedent


def main_menu():
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
                crud_menu()
            case '2':
                top_ten_menu()
            case _:
                print('Invalid option!')


def crud_menu():
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
        case '1' | '2' | '3' | '4' | '5':
            print('Not implemented!')
        case _:
            print('Invalid option!')


def top_ten_menu():
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


main_menu()
