# # 3.3.2 Class variables
# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
#
# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

# ----------------------------------------
class ExampleClass:
    varia = 1
    def __init__(self, val):
        #ExampleClass.varia = val
        varia = val
        self.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(ExampleClass.__dict__['varia'])
print(example_object.__dict__)
