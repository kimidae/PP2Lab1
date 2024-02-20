def evennum(start, stop):
    while (start<=stop):
        yield start
        start+=2
    
n=int(input())
mytuple=tuple(evennum(0, n))
strtuple=map(str, mytuple)
newtuple=", ".join(strtuple)
print (newtuple)