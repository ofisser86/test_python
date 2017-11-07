from datetime import timedelta, date

myear, mmonth, mday = input().split(' ')
days = int(input())
c = date(int(myear), int(mmonth), int(mday)) + timedelta(days=days)
print(c.year, c.month, c.day)

# Teacher solution
import datetime

y, m, d = map(int, input().split())
days = int(input())

current = datetime.date(year=y, month=m, day=d)
current += datetime.timedelta(days=days)

print("{} {} {}".format(current.year, current.month, current.day))