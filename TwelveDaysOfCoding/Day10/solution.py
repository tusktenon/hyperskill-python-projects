dataset = 'hyperskill-dataset-119174654.txt'

sequences = []
with open(dataset) as file:
    for line in file:
        sequences.append(line.rstrip().replace(',', ''))

m = len(sequences)  # number of sequences
n = len(sequences[0])  # length of each sequence
lcs = 0  # length of longest common substring

for i in range(0, n):
    # don't bother checking subsequences that are shorter than current lcs:
    for j in range(i + lcs + 1, n):
        current_subsequence = sequences[0][i:j]
        if len([s for s in sequences[1:] if s.find(current_subsequence) != -1]) == m - 1:
            lcs = j - i

print('Length of longest common contiguous subsequence:', lcs)
