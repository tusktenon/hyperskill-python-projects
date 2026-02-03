left, op, right = input().split()
left, right = int(left), int(right)
match op:
    case '+':
        print(left + right)
    case '-':
        print(left - right)
    case '*':
        print(left * right)
    case _:
        raise ValueError('Unknown operator: ' + op)
