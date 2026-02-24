def get_board_dimensions():
    while True:
        try:
            cols, rows = map(int, input('Enter your board dimensions: ').split())
            if cols < 0 or rows < 0:
                raise ValueError()
        except ValueError:
            print('Invalid dimensions!')
        else:
            return cols, rows


def get_starting_position(cols, rows):
    while True:
        try:
            file, rank = map(int, input("Enter the knight's starting position: ").split())
            if not (1 <= file <= cols and 1 <= rank <= rows):
                raise ValueError()
        except ValueError:
            print('Invalid position!')
        else:
            return file, rank


def is_possible_move(file, rank, knight_file, knight_rank):
    if abs(file - knight_file) == 1:
        return abs(rank - knight_rank) == 2
    if abs(rank - knight_rank) == 1:
        return abs(file - knight_file) == 2
    return False


def possible_moves(file, rank, knight_file, knight_rank, cols, rows):
    moves = 0
    for m in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        new_file, new_rank = file + m[0], rank + m[1]
        if (
            1 <= new_file <= cols
            and 1 <= new_rank <= rows
            and (new_file, new_rank) != (knight_file, knight_rank)
        ):
            moves += 1
    return moves


def draw_board(start_file, start_rank, cols, rows):
    cell_width = len(str(cols * rows))
    row_number_width = len(str(rows))
    border = row_number_width * ' ' + (cols * (cell_width + 1) + 3) * '-'
    print(border)
    for rank in range(rows, 0, -1):
        print((row_number_width - len(str(rank))) * ' ' + f'{rank}| ', end='')
        for file in range(1, cols + 1):
            print(
                (cell_width - 1) * ' ' + 'X'
                if (file, rank) == (start_file, start_rank)
                else (cell_width - 1) * ' '
                + str(possible_moves(file, rank, start_file, start_rank, cols, rows))
                if is_possible_move(file, rank, start_file, start_rank)
                else cell_width * '_',
                end=' ',
            )
        print('|')
    print(border)
    print((row_number_width + 1) * ' ', end='')
    for file in map(str, range(1, cols + 1)):
        print((cell_width - len(file) + 1) * ' ' + file, end='')
    print()


def main():
    cols, rows = get_board_dimensions()
    start_file, start_rank = get_starting_position(cols, rows)
    draw_board(start_file, start_rank, cols, rows)


if __name__ == '__main__':
    main()
