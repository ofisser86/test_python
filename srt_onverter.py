import re


def main():
    # read file line by line
    file = open("test.srt", "r")
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search(
                '^$', line) is None:
            text += ' ' + line.rstrip('\n')
        text = text.lstrip()
    with open('test2.txt', 'w') as f:
        f.write(text)
    print(text)


main()
