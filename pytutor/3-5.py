# В рішеннях автора невірні значення до третього уроку (превіряв вручну )))
# les = int(input())
# #essons_time = les * 45
# #les_for = les - 1
# #pause1 = (les_for - (les_for // 2)) * 5
# #pause2 = (les_for - (les_for - (les_for // 2))) * 20
# #print(pause1)
# #print(pause2)
# #print(lessons_time)
# #print((lessons_time + pause1 + pause2 + 540)//60, (lessons_time + pause1 + pause2 + 540)%60)
# if les == 1:
#     print(9, 45)
# elif les == 2:
#     print(10, 35)
# elif les == 3:
#     print(11, 35)
# elif les == 4:
#     print(12, 25)
# elif les == 5:
#     print(13, 25)
# elif les == 6:
#     print(14, 15)
# elif les == 7:
#     print(15, 15)
# elif les == 8:
#     print(16, 5)
# elif les == 9:
#     print(17, 5)
# elif les == 10:
#     print(17, 55)
a = int(input())
a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
print(a//60 + 9, a % 60)