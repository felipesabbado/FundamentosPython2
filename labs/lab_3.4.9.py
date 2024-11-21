# Points on a plane
from math import hypot


class Point:
    def __init__(self, x:float=0.0, y:float=0.0):
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


# Main Program
point1 = Point(0, 0)
point2 = Point(1, 1)
point3 = Point(3, 0)
print('Ponto 1 ao Ponto 2:', point1.distance_from_point(point2))
print('Ponto 2 ao P(2, 0):', point2.distance_from_xy(2, 0))
print('Ponto 1 ao Ponto 3:', point1.distance_from_point(point3))
print('Ponto 1 ao P(-2, -2):', point1.distance_from_xy(-2, -2))
