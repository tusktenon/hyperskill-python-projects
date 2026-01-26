results = [int(input()) for _ in range(3)]
mean = sum(results) / 3
print(mean)
if mean >= 60:
    print('Congratulations, you are accepted!')
else:
    print('We regret to inform you that we will not be able to offer you admission.')
