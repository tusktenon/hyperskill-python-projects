import random

expression = f'{random.randint(2, 9)} {random.choice(["+", "-", "*"])} {random.randint(2, 9)}'
print(expression)
print('Right!' if int(input()) == eval(expression) else 'Wrong!')
