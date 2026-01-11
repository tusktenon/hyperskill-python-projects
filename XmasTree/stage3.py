def print_tree(height, interval):
    rows = tree_rows(height, interval)
    spaces = leading_spaces(height)
    for i in range(height + 2):
        print(spaces[i] * ' ' + rows[i])


def tree_rows(height, interval):
    decoration_slot = 0
    rows = ['X', '^']
    for i in range(1, height):
        row = ['/']
        for j in range(2 * i - 1):
            if j % 2 == 1:
                row.append('O' if decoration_slot % interval == 0 else '*')
                decoration_slot += 1
            else:
                row.append('*')
        row.append('\\')
        rows.append(''.join(row))
    rows.append('| |')
    return rows


def leading_spaces(height):
    spaces = [height - 1, height - 1]
    for i in range(height - 2, -1, -1):
        spaces.append(i)
    spaces.append(height - 2)
    return spaces


def main():
    height, interval = map(int, input('Tree height and decoration interval: ').split())
    print_tree(height, interval)


if __name__ == '__main__':
    main()
