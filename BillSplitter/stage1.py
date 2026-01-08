n = int(input('Enter the number of friends joining (including you): '))
if n < 1:
    print('\nNo one is joining for the party')
else:
    friends = {}
    print('\nEnter the name of every friend (including you), each on a new line:')
    for i in range(n):
        friends[input()] = 0
    print(f'\n{friends}')
