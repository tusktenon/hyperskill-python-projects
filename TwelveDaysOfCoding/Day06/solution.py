from operator import itemgetter

dataset = 'hyperskill-dataset-119096963.txt'

# A map of nodes to their distance from the starting node
distances = {}

# A map of nodes to their neighbours
neighbours = {}

# Working queue of nodes to visit
queue = []

# Set of previously visited nodes
visited = set()

# From the dataset, read the starting node and build the neighbours map
with open(dataset) as file:
    starting_node = file.readline().rstrip()
    for line in file:
        first, second = line.rstrip().split(',')
        neighbours[first] = neighbours.get(first, set())
        neighbours[first].add(second)
        neighbours[second] = neighbours.get(second, set())
        neighbours[second].add(first)

# Perform breadth-first search
distances[starting_node] = 0
visited.add(starting_node)
queue.append(starting_node)

while queue:
    current = queue.pop(0)
    for neighbour in neighbours[current]:
        if neighbour not in visited:
            distances[neighbour] = distances[current] + 1
            visited.add(neighbour)
            queue.append(neighbour)

# Sort nodes alphabetically, then (stable) sort again by distance
distances = list(distances.items())
distances.sort(key=itemgetter(0))
distances.sort(key=itemgetter(1), reverse=True)
print(distances)
