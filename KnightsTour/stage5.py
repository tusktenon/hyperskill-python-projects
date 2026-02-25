from io import StringIO


class KnightsTour:
    def __init__(self, cols, rows, file, rank):
        self.cols = cols
        self.rows = rows
        self.file = file
        self.rank = rank
        self.visited = {(file, rank)}

    @classmethod
    def from_prompt(cls):
        cols, rows = cls._get_board_dimensions()
        file, rank = cls._get_starting_position(cols, rows)
        return cls(cols, rows, file, rank)

    def play(self):
        print(self)
        while True:
            self._get_next_move()
            print(self)
            if len(self.visited) == self.cols * self.rows:
                print('What a great tour! Congratulations!')
                return
            if not self._possible_moves(self.file, self.rank):
                print('No more possible moves!')
                print(f'Your knight visited {len(self.visited)} squares!')
                return

    def __str__(self):
        cell_width = len(str(self.cols * self.rows))
        row_number_width = len(str(self.rows))
        border = row_number_width * ' ' + (self.cols * (cell_width + 1) + 3) * '-'
        out = StringIO()
        out.write(border + '\n')
        for rank in range(self.rows, 0, -1):
            out.write((row_number_width - len(str(rank))) * ' ' + f'{rank}| ')
            for file in range(1, self.cols + 1):
                out.write(self._symbol(file, rank, cell_width) + ' ')
            out.write('|\n')
        out.write(border + '\n')
        out.write((row_number_width + 1) * ' ')
        for file in map(str, range(1, self.cols + 1)):
            out.write((cell_width - len(file) + 1) * ' ' + file)
        out.write('\n')
        result = out.getvalue()
        out.close()
        return result

    @staticmethod
    def _get_board_dimensions():
        while True:
            try:
                cols, rows = map(int, input('Enter your board dimensions: ').split())
                if cols < 0 or rows < 0:
                    raise ValueError()
            except ValueError:
                print('Invalid dimensions!')
            else:
                return cols, rows

    @staticmethod
    def _get_starting_position(cols, rows):
        while True:
            try:
                file, rank = map(int, input("Enter the knight's starting position: ").split())
                if not (1 <= file <= cols and 1 <= rank <= rows):
                    raise ValueError()
            except ValueError:
                print('Invalid position!')
            else:
                return file, rank

    def _get_next_move(self):
        while True:
            try:
                file, rank = map(int, input('Enter your next move: ').split())
                if (file, rank) not in self._possible_moves(self.file, self.rank):
                    raise ValueError()
            except ValueError:
                print('Invalid move!', end=' ')
            else:
                self.file = file
                self.rank = rank
                self.visited.add((file, rank))
                return

    def _is_possible_move(self, new_file, new_rank):
        if (new_file, new_rank) in self.visited:
            return False
        if abs(new_file - self.file) == 1:
            return abs(new_rank - self.rank) == 2
        if abs(new_rank - self.rank) == 1:
            return abs(new_file - self.file) == 2
        return False

    def _possible_moves(self, file, rank):
        relative_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        moves = [(file + m[0], rank + m[1]) for m in relative_moves]
        return [
            m
            for m in moves
            if 1 <= m[0] <= self.cols and 1 <= m[1] <= self.rows and m not in self.visited
        ]

    def _symbol(self, file, rank, width):
        if (file, rank) == (self.file, self.rank):
            return (width - 1) * ' ' + 'X'
        if (file, rank) in self.visited:
            return (width - 1) * ' ' + '*'
        if self._is_possible_move(file, rank):
            return (width - 1) * ' ' + str(len(self._possible_moves(file, rank)))
        return width * '_'


KnightsTour.from_prompt().play()
