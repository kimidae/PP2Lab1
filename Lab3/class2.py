class Shape:
    def __init__(self):
        self.area = 0
    
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def calculate_area(self):
        self.area = self.length ** 2
print ("Length of one side:")
num=int(input())
s = Square(num)
s.calculate_area()
print("Area of square:", s.area)
