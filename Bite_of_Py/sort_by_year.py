students = ["dima_1986", "maria_1987", "taras_2000", "olya_1999"]


def year(name):
    return name.split('_')[-1]


s = sorted(students, key=year)
print(s)
