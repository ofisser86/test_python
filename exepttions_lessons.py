def f(x, y):
    try:
        return x / y
    except Exception:
        print("Some error here")

print(f(10,0))