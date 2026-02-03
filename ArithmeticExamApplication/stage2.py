import random

ops = [('+', int.__add__), ('-', int.__sub__), ('*', int.__mul__)]
op = ops[random.randrange(3)]
left = random.randint(2, 9)
right = random.randint(2, 9)
print(left, op[0], right)
print('Right!' if int(input()) == op[1](left, right) else 'Wrong!')
