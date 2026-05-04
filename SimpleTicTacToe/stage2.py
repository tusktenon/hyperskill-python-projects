grid = input()
print('---------')
for i in range(3):
    print('| ' + ' '.join(grid[3 * i : 3 * i + 3]) + ' |')
print('---------')
