import requests, re
from bs4 import BeautifulSoup

# input_url = input()
with open('url.html', 'r') as f:
    for line in f:
        soup = BeautifulSoup(line.strip(), 'html.parser')
        print(soup.find_all("a", href=re.compile("elsie")))
        #print(line.strip())

# res = requests.get(input_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all("a"))
import requests
import re
res = requests.get(input().rstrip())
linkset = set()

if res.status_code == 200:

    pattern = re.compile(r'(?:<a.+?href=.)(\w.+?)(?:[\S\s]>)', re.IGNORECASE)
    pattern2 = re.compile(r'^(?:\w+://|\b)(.+?)(?:["\'\ ].*|[/:].*|\b)$', re.IGNORECASE)
    match = pattern.findall(res.text)

    for i in match:
        match2 = pattern2.findall(i)
        linkset.add(match2[0])

for i in sorted(list(linkset)):
    print(i)