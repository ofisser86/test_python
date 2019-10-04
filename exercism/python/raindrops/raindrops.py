def convert(number):
    res = ''
    if number % 3 == 0:
        res = 'Pling'

    if number % 5 == 0:
        res += 'Plang'

    if number % 7 == 0:
        res += 'Plong'

    if len(res) > 0:
        return res
    else:
        return str(number)


print(convert(21))
""" Other better solution

def convert(number):
    s = ''
    words = {3:'Pling',5:'Plang',7:'Plong'}
    for key in words.keys():
        s += words[key] if number%key == 0 else ''
    return str(number) if s == '' else s
    
"""


