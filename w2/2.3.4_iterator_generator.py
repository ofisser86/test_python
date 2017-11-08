import itertools

number_list = range(-5, 5)
less_than_zero = list(filter(1, number_list))
print(less_than_zero)
# =============================================
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
 # <itertools.permutations object at 0xb754f1dc>
print(list(itertools.permutations(horses)))