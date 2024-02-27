import math
n=float(input("Input number of sides: "))
a=float(input("Input the length of a side: "))

s=n*a**2/(4*math.tan(math.pi/n))
print ("Input the length of a side: ", s)