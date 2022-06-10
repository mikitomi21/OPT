import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int(round(self.distance, 0))

p1 = Point(2,5)
p2 = Point(4,5)
p3 = p1+p2
p4 = Point(2,5)
print(len(p1))
print(p1.distance)