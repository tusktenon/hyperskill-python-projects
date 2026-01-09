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
    splits = {friend: round(total / n, 2) for friend in friends}
    print(f'\n{splits}')
