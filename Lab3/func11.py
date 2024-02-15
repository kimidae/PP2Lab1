def pol(str):
    for i in range (len(str)):
        if (str[i] is not str[len(str) - i -1]):
            return False
    return True
str=input()
if pol(str): print ("Yes")
else:
    print ("No")