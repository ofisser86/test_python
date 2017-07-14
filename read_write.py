d = {i: [] for i in range(1, 12)}
with open('3380_5 .txt') as f:
    for line in f:
        line = line.split()
        d[int(line[0])].append(float(line[2]))
t = 0
for value in d.values():
    if value == [' ']:
        value = '-'
    else:
        value = sum(value)/len(value)
    t += 1
    print(t, value)
