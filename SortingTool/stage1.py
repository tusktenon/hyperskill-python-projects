numbers = []
while True:
    try:
        numbers += list(map(int, input().split()))
    except EOFError:
        break

greatest = max(numbers)
greatest_count = len([x for x in numbers if x == greatest])

print(f'Total numbers: {len(numbers)}.')
print(f'The greatest number: {greatest} ({greatest_count} time(s)).')
