n = int(input('Enter the number of friends joining (including you): '))
if n < 1:
    print('\nNo one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    friends = {input(): 0 for _ in range(n)}
    print(f'\n{friends}')
