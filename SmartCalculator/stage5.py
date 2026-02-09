def evaluate(expression):
    terms = expression.split()
    while len(terms) > 1:
        a, op, b, *terms = terms
        a, b = int(a), int(b)
        terms.insert(0, a + b if op.count('-') % 2 == 0 else a - b)
    return int(terms[0])


def main():
    while (user_input := input()) != '/exit':
        if user_input == '/help':
            print('The program calculates sums and differences of any length')
        elif user_input.startswith('/'):
            print('Unknown command')
        elif user_input:
            try:
                print(evaluate(user_input))
            except ValueError:
                print('Invalid expression')
    print('Bye!')


if __name__ == '__main__':
    main()
