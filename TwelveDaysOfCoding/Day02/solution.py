from itertools import product

dataset = 'hyperskill-dataset-118989632.txt'

with open(dataset) as file:
    target = int(file.readline())
    varieties = [int(s) for s in file.readline().split(',')]

delta = min(abs(x + y - 2 * target) for (x, y) in product(varieties, varieties))
closest_average = int((delta + 2 * target) / 2)
print(closest_average)
