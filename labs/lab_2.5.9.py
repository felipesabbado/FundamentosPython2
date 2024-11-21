# The Digit of Life
bdate = input('Enter your birthday: ').replace('-', '').replace(' ', '').replace('\\', '')

while len(bdate) > 1:
    s = 0
    for c in bdate:
        s += int(c)
    bdate = str(s)

print(bdate)
