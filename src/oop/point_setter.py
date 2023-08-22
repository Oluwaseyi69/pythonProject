class Point:
    color = "blue"

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.__point_b = point_b


    @property
    def point_a(self):
        return self.__point_a


    @point_a.setter
    def point_a(self, value):
        if value < 0:
            raise ValueError("value cannot be negative")
        self.__point_a = value

    def draw(self):
        print(f"drawing from point {self.__point_a} to {self.__point_b}")

    def __str__(self):
        return f"({self.__point_a}, {self.__point_b})"
    def __eq__(self, other):
        return self.__point_a == other.value_a and self.__point_b == other.point_b
    def __add__(self, other):
        return f'({self.__point_a + self.__point_a}, {self.__point_b + self.__point_b})'
    def __mod__(self, other):
        return f'({self.__point_b % self.__point_a})'


Point.color = "red"
p1 = Point(12, 4)
p2 = Point(3, 2)
print(p1 + p2)
print(p1%p2)

print(p1.point_a)
print(p2.color)