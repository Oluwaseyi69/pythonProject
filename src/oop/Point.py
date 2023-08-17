class Point:
    # constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # instance method
    def draw(self):
        print("drawing")
        print(f"({self.a}, {self.b})")
    # to string method
    def __str__(self):
        return f"({self.a}, {self.b})"

p1 = Point(1, 2)
p2 = Point(5, 6)
print(p1,p2)
