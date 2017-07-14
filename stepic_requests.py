import requests

# strA = input().split()
# strB = input().split()

strA = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
strB = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
resA = requests.get(strA)
resB = requests.get(strB)
print(resA.text)
for i in resA.text:
    pass

# print(resA.text)
#
# if strB not in resA.text:
#     aA = resA.text
#     aB = resB.text
#     if aA == aB:
#         print("Yes")
#     else:
#         print("NoNo")
# else:
#     print("No")
