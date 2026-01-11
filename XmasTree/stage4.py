CARD_HEIGHT = 30
CARD_WIDTH = 50
MESSAGE = 'Merry Xmas'


def display_canvas(canvas):
    for row in canvas:
        print(''.join([col for col in row]))


def draw_tree(height, interval):
    canvas = [(2 * height - 1) * [' '] for _ in range(height + 2)]

    # Draw star, tip and trunk
    canvas[0][height - 1] = 'X'
    canvas[1][height - 1] = '^'
    canvas[height + 1][height - 2] = '|'
    canvas[height + 1][height] = '|'

    # Draw tree body and decorations
    decoration_slot = 0
    for i in range(2, height + 1):
        canvas[i][height - i] = '/'
        for j in range(1 - i, i - 2):
            if (j - i) % 2 == 0:
                canvas[i][height + j] = 'O' if decoration_slot % interval == 0 else '*'
                decoration_slot += 1
            else:
                canvas[i][height + j] = '*'
        canvas[i][height + i - 2] = '\\'

    return canvas


def draw_card(*args):
    card = [CARD_WIDTH * [' '] for _ in range(CARD_HEIGHT)]
    while args:
        current, args = args[0:4], args[4:]
        draw_offset_tree(card, *current)
    draw_frame(card)
    draw_message(card)
    return card


def draw_offset_tree(card, height, interval, start_row, start_col):
    tree_canvas = draw_tree(height, interval)
    for i in range(height + 2):
        for j in range(2 * height - 1):
            if tree_canvas[i][j] != ' ':
                card[start_row + i][start_col - height + 1 + j] = tree_canvas[i][j]


def draw_frame(card):
    for j in range(CARD_WIDTH):
        card[0][j] = '-'
        card[-1][j] = '-'
    for i in range(1, CARD_HEIGHT - 1):
        card[i][0] = '|'
        card[i][-1] = '|'


def draw_message(card):
    start = (CARD_WIDTH - len(MESSAGE)) // 2
    for j, letter in enumerate(MESSAGE):
        card[CARD_HEIGHT - 3][start + j] = letter


def main():
    args = [int(arg) for arg in input().split()]
    if len(args) == 2:
        # Print tree only
        display_canvas(draw_tree(*args))
    else:
        # Print card
        display_canvas(draw_card(*args))


if __name__ == '__main__':
    main()
