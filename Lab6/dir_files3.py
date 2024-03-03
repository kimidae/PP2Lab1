import os

mypath= input("Path:")
if os.path.exists(mypath):
    print ("The path exists")
else:
    print ("The path does not exist")
