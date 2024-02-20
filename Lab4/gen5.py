def evennum(start, stop):
    while start >= stop:
        yield start
        start-=1
    
n=int(input())
mytuple=tuple(evennum(n, 0))
strtuple=map(str, mytuple)
newtuple=", ".join(strtuple)
print (newtuple)