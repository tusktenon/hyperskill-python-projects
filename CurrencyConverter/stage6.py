import json

import requests


def lookup(rates, source, *targets):
    req = requests.get('http://www.floatrates.com/daily/' + source.lower() + '.json')
    res = json.loads(req.text)
    for target in targets:
        if source == target:
            rates[target] = 1
        else:
            rates[target] = res[target.lower()]['rate']


def main():
    rates = {}
    source = input().upper()
    lookup(rates, source, 'USD', 'EUR')
    while target := input().upper():
        amount = float(input())
        print('Checking the cache...')
        if rates.get(target):
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            lookup(rates, source, target)
        print(f'You received {round(amount * (rates[target]), 2)} {target}.')


if __name__ == '__main__':
    main()
