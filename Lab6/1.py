from functools import reduce
mylist= [1, 2, 3, 4, 5]
res=reduce(lambda x, y: x*y, mylist)
print (res)

"""
res = 1
for x in mylist:
    res *= x
print (res)
"""