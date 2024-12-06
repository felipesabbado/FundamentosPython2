def fun(n):
    s = '+'
    for i in range(2):
        s += s
        yield s


for x in fun(2):
    print(x, end='')

print()

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())
