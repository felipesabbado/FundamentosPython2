# OOP Fundamentals: Inheritance
# 3.5.2 issubclass()
# issubclass(ClassOne, ClassTwo)
# The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# Main program
classes = [Vehicle, LandVehicle, TrackedVehicle]
for cls1 in classes:
    print(f'Is {cls1.__name__} subclass of:')
    for cls2 in classes:
        print(f'\t{cls2.__name__}?', issubclass(cls1, cls2))
