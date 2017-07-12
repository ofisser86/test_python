import requests

strA = str(input())
strB = str(input())

resA = requests.get(strA)
resB = requests.get(strB)
print(resA.url)
print(resA.text)

if '<a href="B">' not in resA.text:

else:
    print("No")