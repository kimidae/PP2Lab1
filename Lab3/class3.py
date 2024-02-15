class Shape:
    def init(self):
        self.area = 0
    
    def calculate_area(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().init()
        self.length = length
        self.width = width
    
    def calculate_area(self):
        self.area = self.length * self.width

print ("Length of first side:")
a=int(input())
print ("Length of second side:")
b=int(input())
r = Rectangle(a, b)
r.calculate_area()
print("Rectangle area is:", r.area)