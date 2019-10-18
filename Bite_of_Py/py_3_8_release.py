"""
    Some new features in Python 3.8

"""
walrus = False
print(walrus)

print(walrus := True)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)

print(inputs)