# f = open('test.txt')
# for line in f:
#     print(repr(line))

# f.close()
# =====================write to file=============
f = open('test1.txt', 'w')
line = ['Line1','Line2','Line3']
content = '\n'.join(line)
f.write(content)
f.close()

f1 = open('test1.txt', 'a')
f1.write('\nhello\n')
f1.close()