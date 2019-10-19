class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print(f"Hello, my name is {self.name}")
# Пустой блок


p = Person("Dima")


p.sayHi()
