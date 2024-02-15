import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The coordinates of the point are: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(1, 2)

point1.show()

point1.move(3, -1)
point1.show()

point2 = Point(4, 6)

distance = point1.dist(point2)
print(distance)
