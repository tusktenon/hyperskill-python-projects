from math import ceil

principal = int(input('Enter the loan principal: '))

calculation = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment: """)

match calculation:
    case 'm':
        payment = int(input('Enter the monthly payment: '))
        months = ceil(principal / payment)
        print(f'\nIt will take {months} {'months' if months > 1 else 'month'} to repay the loan.')
    case 'p':
        months = int(input('Enter the number of months: '))
        regular = ceil(principal / months)
        if principal % regular == 0:
            print(f'\nYour monthly payment = {regular}.')
        else:
            final = principal - (months - 1) * regular
            print(f'\nYour monthly payment = {regular} and the last payment = {final}.')
    case _:
        print('\nInvalid response.')
