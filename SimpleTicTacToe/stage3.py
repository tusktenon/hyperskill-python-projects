grid = input()

print('---------')
for i in range(3):
    print('| ' + ' '.join(grid[3 * i : 3 * i + 3]) + ' |')
print('---------')


def wins(player):
    lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    return any([all([grid[i] == player for i in line]) for line in lines])


x_wins = wins('X')
o_wins = wins('O')

if (x_wins and o_wins) or abs(grid.count('X') - grid.count('O')) > 1:
    print('Impossible')
elif x_wins:
    print('X wins')
elif o_wins:
    print('O wins')
elif '_' not in grid:
    print('Draw')
else:
    print('Game not finished')
