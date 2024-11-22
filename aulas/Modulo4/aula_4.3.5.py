"""4.3.5 What is a bytearray?"""
# it's an array containing (amorphous) bytes.

from os import strerror

data = bytearray(10)
print(data)

for i in range(len(data)):
    data[i] = ord('a') + i

for b in data:
    print('\\'+hex(b), end='')
print()

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print('I/O error ocurred:', strerror(e.errno))
