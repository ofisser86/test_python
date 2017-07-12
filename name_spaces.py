students = []
n = int(input())
for i in range(0, n):
    s = input().replace(' ', '').split(':')
    students.append({'name': s})

print(students)

