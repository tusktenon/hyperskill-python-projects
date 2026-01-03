import math
from queue import PriorityQueue

dataset = 'hyperskill-dataset-119155144.txt'
ROWS = 20
COLS = 20


def neighbours(x, y):
    """Returns the neighbouring cells of (x,y) as a list of tuples."""
    _neighbours = []
    if x > 0:
        _neighbours.append((x - 1, y))
    if x < ROWS - 1:
        _neighbours.append((x + 1, y))
    if y > 0:
        _neighbours.append((x, y - 1))
    if y < COLS - 1:
        _neighbours.append((x, y + 1))
    return _neighbours


def display_matrix(m):
    """For debugging. Prints a nicely formatted 2 x 2 matrix."""
    for row in m:
        for entry in row:
            print(f'{entry:>3}', end=' ')
        print()


costs = []
with open(dataset) as file:
    i = 0
    for line in file:
        costs.append([])
        j = 0
        for cost in line.rstrip().split(','):
            costs[i].append(int(cost))
            j += 1
        i += 1

distances = []
for row in range(0, ROWS):
    distances.append(COLS * [math.inf])
distances[0][0] = 0

queue = PriorityQueue()
queue.put((costs[0][0], (0, 0)))

# Dijkstra's algorithm
while not queue.empty():
    currentDistance, (x, y) = queue.get()
    for u, v in neighbours(x, y):
        newDistance = currentDistance + costs[u][v]
        if newDistance < distances[u][v]:
            distances[u][v] = newDistance
            queue.put((newDistance, (u, v)))

print('Costs matrix:')
display_matrix(costs)
print('\nDistances matrix:')
display_matrix(distances)
print('\nMinimum cost to reach bottom-right cell:', distances[19][19])
