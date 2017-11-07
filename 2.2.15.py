from datetime import timedelta, date

myear, mmonth, mday = input().split(' ')
days = int(input())
c = date(int(myear), int(mmonth), int(mday)) + timedelta(days=days)
print(c.year, c.month, c.day)