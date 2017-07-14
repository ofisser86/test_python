import requests

with open('dataset_24476_3.txt', 'r') as number:
    num = number.read().splitlines()
    print(num)
    for i in num:
        api_url = 'http://numbersapi.com/{}/math?json=true'.format(i)
        data = requests.get(api_url)
        res = data.json()
        if res['found']:
            print('Interesting')
        else:
            print('Boring')
#print(res['found'])