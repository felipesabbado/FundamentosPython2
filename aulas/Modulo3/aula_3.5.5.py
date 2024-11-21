# OOP Fundamentals: Inheritance
# 3.5.5 How Python finds properties and methods

class Super:
    def __init__(self, name='Super'):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name='Sub'):
        Super.__init__(self, name)
        # super().__init__(name)


no_named_obj = Sub()
named_obj = Sub('Andy')

print(no_named_obj)
print(named_obj)
