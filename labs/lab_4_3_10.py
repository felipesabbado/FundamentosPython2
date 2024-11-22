"""Evaluating students' results"""
from os import strerror

class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line_number=0, line_string=''):
        StudentsDataException.__init__(self)
        if line_string in ' \n\t':
            self.line_string = 'Empty line'
        else:
            self.line_string = line_string
        self.line_number = line_number


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


# Main program
if __name__ == '__main__':
    #file_name = input('Enter student\'s data filename: ')
    file_name = 'studentsfile2.txt'
    students = dict()
    l_number = 0

    try:
        file = open(file_name, 'rt')
        for line in file:
            l = line.strip().split()
            l_number += 1
            if len(l) != 3:
                raise WrongLine(l_number, line)
            name = l[0] + ' ' + l[1]
            try:
                score = float(l[2])
            except ValueError:
                raise WrongLine(l_number, line)
            if name not in students:
                students[name] = 0
            students[name] += score
        file.close()
        if len(students) == 0:
            raise FileEmpty
        for k, v in sorted(students.items()):
            print(f'{k}\t\t{v}')
    except IOError as e:
        print('I/O error occurred:', strerror(e.errno))
    except WrongLine as e:
        print(f'Wrong line #{e.line_number} in source file:', e.line_string)
    except FileEmpty:
        print('Source file empty')

