def evaluate(expression):
    terms = expression.split()
    while len(terms) > 1:
        a, op, b, *terms = terms
        a, op, b = int(a), _parse_op(op), int(b)
        terms.insert(0, op(a, b))
    return terms[0]


def _parse_op(string):
    return int.__add__ if string.count('-') % 2 == 0 else int.__sub__


def main():
    while (user_input := input()) != '/exit':
        if user_input == '/help':
            print('The program calculates sums and differences of any length')
        elif user_input:
            print(evaluate(user_input))
    print('Bye!')


if __name__ == '__main__':
    main()
