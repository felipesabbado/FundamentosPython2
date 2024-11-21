# OOP Fundamentals: Inheritance
# 3.5.3 isinstance()
# isinstance(objectName, ClassName)
# The function returns True if the object is an instance of the class, or False otherwise.

class Vehicle:
    # name = 'my_vehicle'
    def __init__(self):
        self.name = 'my_vehicle'

    def __str__(self):
        return self.name


class LandVehicle(Vehicle):
    # name = 'my_land_vehicle'
    def __init__(self):
        Vehicle.__init__(self)
        self.name = 'my_land_vehicle'


class TrackedVehicle(LandVehicle):
    def __init__(self):
        super().__init__()
        self.name = 'my_tracked_vehicle'


# Main program
vehicle = Vehicle()
land_vehicle = LandVehicle()
tracked_vehicle = TrackedVehicle()
vehicles = [vehicle, land_vehicle, tracked_vehicle]
classes = [Vehicle, LandVehicle, TrackedVehicle]

for obj in vehicles:
    print(f'Is {obj} instance of:')
    for cls in classes:
        print(f'\t{cls.__name__}?', isinstance(obj, cls))

