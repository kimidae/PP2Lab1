def isupper(x):
    if ('A'<x and x<'Z'):
        return True
    return False
def islower(x):
    if ('a'<x and x<'z'):
        return True
    return False

mystring="I waNna be yOur vaCUUm cLEaner. BreAthINg in your dUst"
upperlist=list(map(isupper, mystring))
uppersum = sum(upperlist)
lowerlist=list(map(islower, mystring))
lowersum = sum(lowerlist)
print("Uppers:", uppersum, "Lowers:", lowersum)