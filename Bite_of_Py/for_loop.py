children = ["dima_1986", "maria_1987", "taras_2000", "olya_1999"]

child_names = []
for child in children:
    # divide names and year
    child_part = child.split("_")[0].title()
    child_names.append(child_part)

print(" ".join(child_names))

teacher = ['Petrivna', 'Ivanivna', 'Olehivna']
children.append(teacher)
print(children)