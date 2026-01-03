dataset = 'hyperskill-dataset-119129056.txt'


def can_attack(a, b):
    return a[0] == b[0] or a[1] == b[1] or abs(a[0] - b[0]) == abs(a[1] - b[1])


positions = []
with open(dataset) as file:
    for line in file:
        row, col = line.rstrip().split(',')
        positions.append((int(row), int(col)))

conflicts = 0
for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        if can_attack(positions[i], positions[j]):
            print(f'Queen {i} is attacking Queen{j}')
            conflicts += 1

print('Total conflicts:', conflicts)
