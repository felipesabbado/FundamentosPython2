# Reading ints safely

def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt).strip())
            assert min <= value <= max
            break
        except ValueError:
            print('Error: wrong input')
        except AssertionError:
            print(f'Error: the value is not within permitted range ({min}..{max})')
        except:
            print('Something goes wrong.')
    return value




v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
