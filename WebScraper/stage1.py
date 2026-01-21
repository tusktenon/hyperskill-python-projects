import requests

url = input('Input the URL: ')
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers)
if response and (joke := response.json().get('joke')):
    print(joke)
else:
    print('Invalid resource!')
