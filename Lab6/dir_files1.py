import os

mypath= r"C:\Users\Юзер\Desktop\program\PP2Labs\Lab6"
listdir=[]
listfile=[]
listall=os.listdir(mypath)
for x in listall:
    if os.path.isdir(x):
        listdir.append(x)
    else:
        listfile.append(x)
print ("Directories:", ", ".join(listdir))
print("------")
print ("Files and directories:", ', '.join(listall))
print("------")
print("Files:", ', '.join(listfile))
