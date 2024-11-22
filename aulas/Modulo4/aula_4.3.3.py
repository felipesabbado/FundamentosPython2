"""4.3.3 readlines()"""

# stream = open("text.txt")
# lines = stream.readlines(31)
# for line in lines:
#     print('Number of bytes:', len(line.encode('utf-8')))
#     print(line, end='')
# stream.close()

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(15)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print('\n\nCharacters in file:', ccnt)
    print('Lines in file:       ', lcnt)
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
print('\n')

"""The object returned by the open() function in text mode is an instance of the iterable class"""
try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
