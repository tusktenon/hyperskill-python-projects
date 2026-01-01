import argparse
from math import ceil, log


def process_args(args):
    if args.interest is None:
        print('"--interest" argument is required')
        return

    a = args.payment
    i = args.interest / (12 * 100)
    n = args.periods
    p = args.principal

    if len([x for x in [a, n, p] if x is not None]) != 2:
        print('Exactly two of "--payment", "--periods", and "--principal" arguments are required')
        return

    return (a, i, n, p)


def calculate_payment(i, n, p):
    x = (1 + i) ** n
    return ceil(p * i * x / (x - 1))


def calculate_periods(a, i, p):
    return ceil(log(a / (a - i * p), 1 + i))


def calculate_principal(a, i, n):
    x = (1 + i) ** n
    return round(a * (x - 1) / (i * x))


def format_months(months):
    y, m = divmod(months, 12)
    year_str = f'{y} year{"s" * (y != 1)}'
    month_str = f'{m} month{"s" * (m != 1)}'
    return f'{year_str * (y > 0)}{" and " * (y > 0 and m > 0)}{month_str * (m > 0)}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--principal', type=float)

    if (args := process_args(parser.parse_args())) is None:
        return
    a, i, n, p = args

    if a is None:
        print(f'Your monthly payment = {calculate_payment(i, n, p)}!')
    elif n is None:
        print(f'It will take {format_months(calculate_periods(a, i, p))} to repay this loan!')
    elif p is None:
        print(f'Your loan principal = {calculate_principal(a, i, n)}!')


if __name__ == '__main__':
    main()
