numbers = []
while True:
    try:
        numbers += list(map(int, input().split()))
    except EOFError:
        break

greatest = max(numbers)

print(f'Total numbers: {len(numbers)}.')
print(f'The greatest number: {greatest} ({numbers.count(greatest)} time(s)).')
