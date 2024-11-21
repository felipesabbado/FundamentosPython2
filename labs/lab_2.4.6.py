# 2.4.6   LAB   A LED Display

patterns = ('#  ', '  #', '# #', '###')
nums = ((3, 2, 2, 2, 3), # 0
        (1, 1, 1, 1, 1), # 1
        (3, 1, 3, 0, 3), # 2
        (3, 1, 3, 1, 3), # 3
        (2, 2, 3, 1, 1), # 4
        (3, 0, 3, 1, 3), # 5
        (3, 0, 3, 2, 3), # 6
        (3, 1, 1, 1, 1), # 7
        (3, 2, 3, 2, 3), # 8
        (3, 2, 3, 1, 3)) # 9


def show_number(number):
    for i in range(5):
        for j in range(len(number)):
            n = int(number[j])
            print(patterns[nums[n][i]], end=' ')
        print()


# Main program
num = input('Digite um número inteiro não negativo: ').strip()

show_number(num)
