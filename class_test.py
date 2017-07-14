#class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#         self.capacity = capacity
#         self.count = 0
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         if self.count + v > self.capacity:
#             return False
#         else:
#             return True
#
#     def add(self, v):
#         # положить v монет в копилку
#         if self.can_add(v):
#             self.count += v
#         else:
#             print('Pig too small :-) ')
#
# x = MoneyBox(10)
# print(x.capacity)
# x.add(1)
# print(x.can_add(10))
# ===============================================================================================================
# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#         self.five = []
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#         self.five.extend(a)
#
#         if len(self.five) >= 5:
#             print(sum(self.five[:5]))
#             self.five = self.five[5:]
#             self.add()
#
#
#         return self.five
#
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
#         return self.five
#
# x = Buffer()
# x.add(1, 2, 3)
# x.get_current_part()
# x.add(4, 5, 6)
# print(x.get_current_part())
# x.add(7,8,9, 10)
# print(x.get_current_part())
# x.add(1,1,1,1,1,1,1,1,1,1,1)
# print(x.get_current_part())
# ================================================================================================================
#
#
# class A:
#     val = 1
#
#     def foo(self):
#         A.val += 2
#
#     def bar(self):
#         self.val += 1
#
#
# a = A()
# b = A()
#
# a.bar()
# a.foo()
#
# c = A()
#
# print(a.val)
# #print(b.val)
# #print(c.val)