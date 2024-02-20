def evennum(start, stop):
    for x in range  (start, stop):
        yield x**2
    
n=int(input())
mytuple=tuple(evennum(0, n))
strtuple=map(str, mytuple)
newtuple=", ".join(strtuple)
print (newtuple)