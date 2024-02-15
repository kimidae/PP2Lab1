def uni(mylist):
    newlist=[]
    for x in mylist:
        if x not in newlist:
            newlist.append(x)
    return newlist
mylist = [1, 2, 3, 3, 4, 4, 5, 4, 1]
print(uni(mylist))