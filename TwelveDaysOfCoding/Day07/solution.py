"""
A connected undirected graph has an Eulerian trial (a walk that uses each edge
exactly once), if and only if exactly zero or two vertices have odd degree.
Otherwise, the minimum number of additional bridge crossings required is
(number of vertices of odd degree / 2) - 1.
"""

from collections import Counter

dataset = 'hyperskill-dataset-119109717.txt'

degrees = Counter()
with open(dataset) as file:
    for line in file:
        first, second = line.rstrip().split(',')
        degrees[first] += 1
        degrees[second] += 1

odd_degrees = len({vertex for vertex in degrees if degrees[vertex] % 2 == 1})
print('Number of vertices of odd degree:', odd_degrees)
print('Number of extra crossings required:', (odd_degrees // 2) - 1)
