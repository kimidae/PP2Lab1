import math
n=float(input("Input number of sides: "))
a=float(input("Input the length of a side: "))

s=n*a**2/(4*math.tan(math.degrees(180)/n))
print (math.tan(math.pi/n), "Input the length of a side: ", s)