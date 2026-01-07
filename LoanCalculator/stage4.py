import argparse
from math import ceil, log


def calculate_annuity(principal, interest, periods, payment):
    if (
        interest is None
        or len([arg for arg in [principal, periods, payment] if arg is None]) != 1
        or any([arg is not None and arg < 0 for arg in [principal, interest, periods, payment]])
    ):
        print('Incorrect parameters')
        return
    interest /= 12 * 100  # Convert from annual to nominal rate
    if principal is None:
        x = (1 + interest) ** periods
        principal = ceil(payment * (x - 1) / (interest * x))
        print(f'Your loan principal = {principal}!')
    elif periods is None:
        periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
        print(f'It will take {_format_months(periods)} to repay this loan!')
    elif payment is None:
        x = (1 + interest) ** periods
        payment = ceil(principal * interest * x / (x - 1))
        print(f'Your monthly payment = {payment}!')
    print('Overpayment =', ceil(periods * payment - principal))


def _format_months(months):
    y, m = divmod(months, 12)
    year_str = f'{y} year{"s" * (y != 1)}'
    month_str = f'{m} month{"s" * (m != 1)}'
    return f'{year_str * (y > 0)}{" and " * (y > 0 and m > 0)}{month_str * (m > 0)}'


def calculate_differentiated(principal, interest, periods):
    if any([arg is None or arg < 0 for arg in [principal, interest, periods]]):
        print('Incorrect parameters')
        return
    interest /= 12 * 100  # Convert from annual to nominal rate
    payments = [
        ceil(principal / periods + interest * (principal - principal * (m - 1) / periods))
        for m in range(1, periods + 1)
    ]
    for i, payment in enumerate(payments):
        print(f'Month {i + 1}: payment is {payment}')
    print('\nOverpayment =', ceil(sum(payments) - principal))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--principal', type=float)
    args = parser.parse_args()

    if args.type == 'annuity':
        calculate_annuity(args.principal, args.interest, args.periods, args.payment)
    elif args.type == 'diff' and args.payment is None:
        calculate_differentiated(args.principal, args.interest, args.periods)
    else:
        print('Incorrect parameters')


if __name__ == '__main__':
    main()
