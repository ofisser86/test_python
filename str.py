s = "ababa"
a = "a"
b = "b"
count = 0


while a in s:
    s = s.replace(a, b)
    if a in s:
        print("Impossible")
    count +=1

print(count)