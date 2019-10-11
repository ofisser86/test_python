def decode(string):
    new_string = ''
    count = 0
    temp = []
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            print(string[i], end=",")
        else:
            pass
            # new_string += str(count + 1) + string[i-1] + string[i]
            # count = 0
            # temp.append((count, string[i-1]))
            # temp.append(string[i])
            # new_string = ''
            # count = 0

    # print(count, end="")
    # print(new_string)
    # print(temp)


def encode(string):
    pass

decode('WWWwBWWWWWBBBWWWWWWWB')