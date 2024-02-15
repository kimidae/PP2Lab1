def solve(numheads, numlegs):
    a=numheads*2
    b=numlegs-a
    return b/2, numheads-b/2
numheads=35
numlegs=94
print(solve(numheads, numlegs))
