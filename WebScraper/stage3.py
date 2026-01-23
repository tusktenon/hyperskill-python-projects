import requests

url = input('Input the URL: ')
response = requests.get(url)
if response:
    with open('source.html', 'wb') as file:
        file.write(response.content)
        print('Content saved.')
else:
    print('The URL returned', response.status_code)
