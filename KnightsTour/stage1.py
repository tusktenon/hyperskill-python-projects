COLS = 8
ROWS = 8

try:
    start_file, start_rank = map(int, input("Enter the knight's starting position: ").split())
    if not (1 <= start_file <= COLS and 1 <= start_rank <= ROWS):
        raise IndexError()
except (IndexError, ValueError):
    print('Invalid dimensions!')
else:
    print((4 + 2 * COLS) * '-')
    for rank in range(ROWS, 0, -1):
        content = [
            'X' if (file, rank) == (start_file, start_rank) else '_' for file in range(1, COLS + 1)
        ]
        print(f'{rank}| ' + ' '.join(content) + ' |')
    print((4 + 2 * COLS) * '-')
    print('   ' + ' '.join(map(str, range(1, COLS + 1))))
