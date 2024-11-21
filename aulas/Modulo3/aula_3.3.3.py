# 3.3.3 Checking an attribute's existence
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


print(hasattr(ExampleClass, 'a'))
print(ExampleClass.a)

example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
