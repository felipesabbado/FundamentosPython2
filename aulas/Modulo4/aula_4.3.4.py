"""4.3.4 Dealing with text files: write()"""
from os import strerror

try:
    file = open('newtext.txt', 'wt') # A new file is created
    for i in range(10):
        s = 'line #' + str(i+1).zfill(2) + '\n'
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
    