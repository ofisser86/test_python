# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

# Одним из атрибутов преступления является его тип – Primary Type.

# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

# Файл с данными:
# Crimes.csv


import csv
from collections import Counter

cnt = Counter()
l = []
with open("Crimes.csv") as crimes:
    reader = csv.DictReader(crimes)
    for row in reader:
        l.append(row['Primary Type'])
        
print(Counter(l).most_common(3))