height = int(input('Tree height: '))
stars, spaces = 1, height - 1
while spaces >= 0:
    print(spaces * ' ' + stars * '*')
    stars += 2
    spaces -= 1
