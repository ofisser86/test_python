print('I am from Uktraine')
length = 5
breadth = 2
area = length * breadth
print('Площадь равна', area)
print('Периметр равен', 2 * (length + breadth))
x = 50


def myfunc(y):
    global x
    y = 1000
    x = y
    print(x)


myfunc(x)


def local_dunc():
    x = 2
    print("x equel", x)

    def inner_func():
        nonlocal x
        x = 5
        print("change x witjh nonocal", x)

    inner_func()


local_dunc()
