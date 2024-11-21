# 3.2 Section 2 – A short journey from procedural to object approach
# 3.2.4 The stack - the object approach

class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


    def push(self, val):
        self.__sum += val
        Stack.push(self, val)


    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


    def get_sum(self):
        return self.__sum


## Main Program
# stack_object_1 = Stack()
# stack_object_2 = Stack()
#
# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())
#
# print(stack_object_2.pop())

stack_obj = AddingStack()

for i in range(5):
    stack_obj.push(i)
print(stack_obj.get_sum())

for i in range(5):
    print(stack_obj.pop())
