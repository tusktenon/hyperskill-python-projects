from string import ascii_letters


class IdentiferError(Exception):
    pass


vars = {}


def assign(statement):
    id, expression = [s.strip() for s in statement.split('=')]
    _check_identifier(id)
    vars[id] = evaluate(expression)


def _check_identifier(name):
    if not all([c in ascii_letters for c in name]):
        raise IdentiferError()


def evaluate(expression):
    tokens = expression.split()
    while len(tokens) > 1:
        a, op, b, *tokens = tokens
        a, op, b = _parse_term(a), _parse_op(op), _parse_term(b)
        tokens.insert(0, op(a, b))
    return _parse_term(tokens[0])


def _parse_term(symbol):
    try:
        return int(symbol)
    except ValueError:
        _check_identifier(symbol)
        return vars[symbol]


def _parse_op(op):
    if not all(x in '+-' for x in op):
        raise ValueError()
    return int.__add__ if op.count('-') % 2 == 0 else int.__sub__


def main():
    while (user_input := input()) != '/exit':
        if user_input == '/help':
            print('The program calculates sums and differences of any length')
        elif user_input.startswith('/'):
            print('Unknown command')
        elif '=' in user_input:
            try:
                assign(user_input)
            except IdentiferError:
                print('Invalid identifier')
            except KeyError:
                print('Unknown variable')
            except ValueError:
                print('Invalid assignment')

        elif user_input:
            try:
                print(evaluate(user_input))
            except IdentiferError:
                print('Invalid identifier')
            except KeyError:
                print('Unknown variable')
            except ValueError:
                print('Invalid expression')
    print('Bye!')


if __name__ == '__main__':
    main()
