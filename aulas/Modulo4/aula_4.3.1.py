"""4.3 Section 3 – Working with real files"""
#stream = open('file.txt', 'rt', encoding='utf-8')

# 4.3.1 Processing text files

from os import strerror
""" # 1st mode: reading char by char
try:
    counter = 0
    stream = open('text.txt', 'rt')
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print('\n\nCharacters in file:', counter)
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
"""

# 2nd mode: reading the whole txt file
try:
    counter = 0
    stream = open('text.txt', 'rt')
    content = stream.read() # be careful with very large files
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print('\n\nCharacters in file:', counter)
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
