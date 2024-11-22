"""4.3.2 readline()"""
from os import strerror

try:
    char_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            char_counter += 1
        line = stream.readline()
    stream.close()
    print('\n\nCharacters in file:', char_counter)
    print('Lines in file:       ', line_counter)
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
