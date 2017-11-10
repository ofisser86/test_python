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