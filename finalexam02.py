import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance(self, other):
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __str__(self):
        return str(self.__x) + ", " + str(self.__y)




p1 = Point(1, 1)
p2 = Point(2, 2)

print("<p1과 p2 사이의 거리>")
print(p1.distance(p2))
print("<p1+p2>")
print(p1 + p2)
