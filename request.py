import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt'.strip(' '))

while r.text.split(' ')[0] != 'We':
    url = r.url.split('/')
    new_url = '/'.join(url[:len(url) - 1]) + '/' + r.text
    r = requests.get(new_url.strip(' '))

print(r.text)
