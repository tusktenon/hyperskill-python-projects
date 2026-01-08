import json

import requests

currency_code = input()
req = requests.get('http://www.floatrates.com/daily/' + currency_code.lower() + '.json')
rates = json.loads(req.text)
print(rates['usd'])
print(rates['eur'])
