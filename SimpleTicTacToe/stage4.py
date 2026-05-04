grid = list(input())


def print_grid():
    print('---------')
    for i in range(3):
        print('| ' + ' '.join(grid[3 * i : 3 * i + 3]) + ' |')
    print('---------')


def get_valid_move():
    while True:
        coords = input().split()
        if not all([c.isdigit() for c in coords]):
            print('You should enter numbers!')
            continue
        row, col = map(int, coords)
        if row < 1 or row > 3 or col < 1 or col > 3:
            print('Coordinates should be from 1 to 3!')
            continue
        move = 3 * (row - 1) + col - 1
        if grid[move] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        return move


print_grid()
grid[get_valid_move()] = 'X'
print_grid()
