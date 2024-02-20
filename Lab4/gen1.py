def squares(start, stop):
    while (start**2<=stop):
        yield start**2
        start+=1
    
n=int(input())
print (list(squares(1, n)))