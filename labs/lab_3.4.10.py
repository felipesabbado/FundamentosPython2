# Points on a plane
from math import hypot


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i, point in enumerate(self.__vertices):
            if i == 0:
                per += point.distance_from_point(self.__vertices[-1])
            else:
                per += point.distance_from_point(self.__vertices[i - 1])
        return per



# Main Program
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
