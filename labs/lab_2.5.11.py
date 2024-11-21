sample_input1 = ('295743861',
                 '431865927',
                 '876192543',
                 '387459216',
                 '612387495',
                 '549216738',
                 '763524189',
                 '928671354',
                 '154938672')

sample_input2 = ('195743862',
                 '431865927',
                 '876192543',
                 '387459216',
                 '612387495',
                 '549216738',
                 '763524189',
                 '928671354',
                 '254938671')

nums = [chr(ord('0') + x) for x in range(1, 10)]

# A function that checks whether a list passed as an argument contains nine digits from '1' to '9'.
def checkset(sample):
    return sorted(list(sample)) == nums

# A list of rows representing the sudoku.
def sudoku_input():
    rows = list()
    for r in range(9):
        ok = False
        while not ok:
            row = input(f'Enter row #{r + 1}: ').strip()
            ok = len(row) == 9 and row.isdigit()
            if not ok:
                print('Incorrect row data - 9 digits required')
        rows.append(row)
    return rows

# Main program
# s = sudoku_input()
s = sample_input1
ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(s[r]):
        ok = False
        break

# Check if all columns are good.
if ok:
    for c in range(9):
        col = list()
        for r in range(9):
            col.append(s[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            for i in range(3):
                sqr += s[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
