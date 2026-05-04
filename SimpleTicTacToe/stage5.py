from io import StringIO


class Game:
    def __init__(self, grid=9 * '_', next='X'):
        self.grid = list(grid)
        self.next = next

    def __str__(self):
        with StringIO() as output:
            output.write('---------\n')
            for i in range(3):
                output.write('| ' + ' '.join(self.grid[3 * i : 3 * i + 3]) + ' |\n')
            output.write('---------\n')
            return output.getvalue()

    def play(self):
        while self.state() == 'Game not finished':
            print(self)
            self.grid[self.get_valid_move()] = self.next
            self.next = 'O' if self.next == 'X' else 'X'
        print(self)
        print(self.state())

    def get_valid_move(self):
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
            if self.grid[move] != '_':
                print('This cell is occupied! Choose another one!')
                continue
            return move

    def state(self):
        x_wins = self.wins('X')
        o_wins = self.wins('O')
        if (x_wins and o_wins) or abs(self.grid.count('X') - self.grid.count('O')) > 1:
            return 'Impossible'
        elif x_wins:
            return 'X wins'
        elif o_wins:
            return 'O wins'
        elif '_' not in self.grid:
            return 'Draw'
        else:
            return 'Game not finished'

    def wins(self, player):
        lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        return any([all([self.grid[i] == player for i in line]) for line in lines])


def main():
    Game().play()


if __name__ == '__main__':
    main()
