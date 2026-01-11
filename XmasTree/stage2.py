height = int(input('Tree height: '))
print((height - 1) * ' ' + 'X')
print((height - 1) * ' ' + '^')
stars, spaces = 1, height - 2
while spaces >= 0:
    print(spaces * ' ' + '/' + stars * '*' + '\\')
    stars += 2
    spaces -= 1
print((height - 2) * ' ' + '| |')
