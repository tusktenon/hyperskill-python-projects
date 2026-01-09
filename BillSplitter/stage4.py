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
    use_lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if use_lucky.capitalize() == 'Yes':
        lucky = random.choice(friends)
        print(f'\n{lucky} is the lucky one!')
        splits = {friend: 0 if friend == lucky else round(total / (n - 1), 2) for friend in friends}
    else:
        print('\nNo one is going to be lucky')
        splits = {friend: round(total / n, 2) for friend in friends}
    print(f'\n{splits}')
