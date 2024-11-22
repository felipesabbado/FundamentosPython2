"""4.3.6 How to read bytes from a stream"""
# readinto() - fills a previously created one with the values taken from the binary file.

from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    #binary_file.readinto(data)
    data = bytearray(binary_file.read(10)) # specifies the maximum number of bytes to be read.
    binary_file.close()

    for b in data:
        print(chr(b), end=' ')
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
