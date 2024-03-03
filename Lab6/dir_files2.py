import os

mypath= r"C:\Users\Юзер\Desktop\program\PP2Labs\Lab6"
listall=os.listdir(mypath)
for x in listall:
        print (f"For {x}:")
        print("Readability:", os.access(x, os.R_OK))
        print("Existance:", os.access(x, os.F_OK))
        print("Writeablity:", os.access(x, os.W_OK))
        print("Executeability:", os.access(x, os.X_OK))
        print("------")
