dataset = 'hyperskill-dataset-119033324.txt'

contentions = 0
available = 4 * [True]

with open(dataset) as file:
    for line in file:
        _, action, fork = line.rstrip().split(',')
        fork = int(fork) - 1
        if action == 'pick':
            if available[fork]:
                available[fork] = False
            else:
                contentions += 1
        elif action == 'release':
            available[fork] = True

print('Contentions:', contentions)
