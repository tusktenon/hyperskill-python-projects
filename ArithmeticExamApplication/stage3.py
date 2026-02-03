import random

mark = 0
for _ in range(5):
    expression = f'{random.randint(2, 9)} {random.choice(["+", "-", "*"])} {random.randint(2, 9)}'
    print(expression)
    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print('Incorrect format.')
    correct = answer == eval(expression)
    print('Right!' if correct else 'Wrong!')
    mark += correct
print(f'Your mark is {mark}/5.')
