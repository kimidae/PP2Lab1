def filter_prime(x):
    if x<2:
        return False
    for i in range (2, int(x/2)+1):
        if x%i==0:
            return False
    return True
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in mylist:
    if filter_prime(x):
        print (x)
