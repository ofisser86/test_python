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

# =====================Authors answers ======================
import re
import requests

start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")