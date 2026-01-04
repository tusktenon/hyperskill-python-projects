import argparse
from math import ceil, log


def calculate(principal, interest, periods, payment):
    if interest is None or len([x for x in [principal, periods, payment] if x is None]) != 1:
        raise TypeError('Invalid arguments')
    interest /= 12 * 100  # Convert from annual to nominal rate
    if principal is None:
        x = (1 + interest) ** periods
        principal = round(payment * (x - 1) / (interest * x))
        print(f'Your loan principal = {principal}!')
    elif periods is None:
        periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
        print(f'It will take {_format_months(periods)} to repay this loan!')
    elif payment is None:
        x = (1 + interest) ** periods
        payment = ceil(principal * interest * x / (x - 1))
        print(f'Your monthly payment = {payment}!')


def _format_months(months):
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
    args = parser.parse_args()

    try:
        calculate(args.principal, args.interest, args.periods, args.payment)
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
