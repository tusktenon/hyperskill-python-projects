import random

try:
    n = int(input('Enter the number of friends joining (including you): '))
    if n < 1:
        raise ValueError()
except ValueError:
    print('\nNo one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    friends = [input() for _ in range(n)]
    total = float(input('\nEnter the total bill value: '))
    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if lucky.capitalize() == 'Yes':
        print(f'\n{random.choice(friends)} is the lucky one!')
    else:
        print('\nNo one is going to be lucky')
