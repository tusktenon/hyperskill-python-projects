import re
from collections import deque

vars = {}


def assign(statement):
    id, expression = [s.strip() for s in statement.split('=')]
    if re.match(r'[a-zA-Z]+$', id):
        vars[id] = evaluate(expression)
    else:
        print('Invalid identifier')


def evaluate(expression):
    return _evaluate_postfix(_convert_to_postfix(expression))


def _convert_to_postfix(infix):
    postfix = []
    ops = deque()
    # Handle case of leading negative sign
    if leading_sign := re.match(r'[+-]+', infix):
        sign, infix = infix[: leading_sign.end()], infix[leading_sign.end() :]
        if sign.count('-') % 2 == 1:
            postfix.append('-1')
            ops.append('*')
    tokens = re.findall(r'[a-zA-Z0-9]+|[*/+-]+|[()]', infix.replace(' ', ''))
    while tokens:
        left, *tokens = tokens
        match left:
            case '(':
                ops.append('(')
            case ')':
                try:
                    while (op := ops.pop()) != '(':
                        postfix.append(op)
                except IndexError:
                    raise ValueError()
            case '*' | '/':
                while ops and ops[-1] in ('*', '/'):
                    postfix.append(ops.pop())
                ops.append(left)
            case _ if re.match(r'[+-]+$', left):
                normalized = '+' if left.count('-') % 2 == 0 else '-'
                while ops and ops[-1] != '(':
                    postfix.append(ops.pop())
                ops.append(normalized)
            case _ if re.match(r'(-?\d+|[a-zA-Z]+)$', left):
                postfix.append(left)
            case _:
                raise ValueError()
    while ops:
        if (op := ops.pop()) == '(':
            raise ValueError()
        else:
            postfix.append(op)
    return postfix


def _evaluate_postfix(postfix):
    ops = {'+': int.__radd__, '-': int.__rsub__, '*': int.__rmul__, '/': int.__rfloordiv__}
    stack = deque()
    while postfix:
        el, *postfix = postfix
        if re.match(r'-?\d+$', el):
            stack.append(int(el))
        elif re.match(r'[a-zA-Z]+$', el):
            stack.append(vars[el])
        elif el in ops:
            stack.append(ops[el](stack.pop(), stack.pop()))
    return stack.pop()


def main():
    while (user_input := input()) != '/exit':
        if user_input == '/help':
            print(
                'Performs integer calculations with addition, subtraction, multiplication, division and parentheses.'
            )
        elif user_input.startswith('/'):
            print('Unknown command')
        elif '=' in user_input:
            try:
                assign(user_input)
            except KeyError:
                print('Unknown variable')
            except ValueError:
                print('Invalid assignment')
        elif user_input:
            try:
                print(evaluate(user_input))
            except KeyError:
                print('Unknown variable')
            except ValueError:
                print('Invalid expression')
    print('Bye!')


if __name__ == '__main__':
    main()
