import requests
from random import random

template = "Response from {0.url} with code {0.status_code}"

res = requests.get('https://docs.python.org/3.5/')
print(template.format(res))

x = random()
print(x)
print('{:.3}'.format(x))