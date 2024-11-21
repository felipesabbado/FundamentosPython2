# 3.2 Section 2 – A short journey from procedural to object approach
# 3.2.2 The stack - the procedural approach

stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
