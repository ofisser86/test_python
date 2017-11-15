import requests
import re
url1, url2 = [input() for _ in range(2)]
# url1 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
# url2 = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
pattern = re.compile(r'(?<=<a href=").{1,}(?=">.*</a>)', re.I)
res = requests.get(url1)
links = pattern.findall(res.text)
c = 0
for i in links:
    ref2 = i
    res2 = requests.get(ref2)
    links2 = pattern.findall(res2.text)
    if url2 in links2:
        c =+ 1
if c == 0:
    print("No")
else:
    print("Yes")