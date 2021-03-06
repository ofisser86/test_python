"""
    Some new features in Python 3.8

"""
walrus = False
print(walrus)

print(walrus := True)

# inputs = list()
# while (current := input("Write something: ")) != "quit":
#     inputs.append(current)
#
# print(inputs)

print(f"Hello".center(100, "+"))


# Python supports optional type hints, typically as annotations on your code:

def double(number: float) -> float:
    return 2 * number