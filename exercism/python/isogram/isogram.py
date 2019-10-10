def is_isogram(string):
    res = False
    try:
        clean_string = string.replace(" ", "").replace('-', '').lower()
    except Exception as ex:
        print("It is not string")
    if len(set(clean_string)) == len(clean_string):
        res = True
    return res
