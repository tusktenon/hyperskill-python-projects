dataset = 'hyperskill-dataset-119059344.txt'

p = []
with open(dataset) as file:
    for line in file:
        x, y = line.rstrip().split(',')
        p.append((float(x), float(y)))

# Using the [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula):
n = len(p)
first, last = p[0], p[-1]
p.insert(0, last)
p.append(first)
area = 0.5 * sum([p[i][0] * (p[i + 1][1] - p[i - 1][1]) for i in range(1, n + 1)])
print(f'Area: {area:.2f}')
