"""Character frequency histogram"""
from os import strerror

def text_analyze(file_name):
    total = 0
    tot_chars = 0
    dic = dict()
    try:
        src = open(file_name, 'r')
        char = src.read(1).lower()
        while char != '':
            if char.isalpha():
                if char not in dic.keys():
                    dic[char] = 0
                dic[char] += 1
                tot_chars += 1
            total += 1
            char = src.read(1).lower()
        src.close()
        print(total, 'byte(s) successfully read')
        print(tot_chars, 'characters read')
        return dic
    except IOError as e:
        print('I/O error occurred:', strerror(e.errno))


# Main program
if __name__ == '__main__':
    #file = input('Enter the name of the file to analyze: ')
    file = 'sample_file.txt'

    counts = text_analyze(file)

    for k in sorted(counts):
        print(k, '->', counts[k])
