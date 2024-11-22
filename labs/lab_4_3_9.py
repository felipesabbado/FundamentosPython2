"""Sorted character frequency histogram"""
from os import strerror, write
from labs.lab_4_3_8 import text_analyze

#file_name = input('Enter the name of the file to analyze: ')
file_name = 'sample_file.txt'

counts = text_analyze(file_name)

counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

try:
    file = open(file_name + '.hist', 'wt')
    for k, v in counts.items():
        s = f'{k} -> {v}\n'
        print(s, end='')
        file.write(s)
    file.close()
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
