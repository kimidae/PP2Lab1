import os

mypath= input("Enter your path:")
print (f"For {mypath}:")
print("Readability:", os.access(mypath, os.R_OK))
print("Writeablity:", os.access(mypath, os.W_OK))
print("Executeability:", os.access(mypath, os.X_OK))
print("------")
if os.path.exists(mypath):
    print ("The path exists")
else:
    print ("The path does not exist")
print ("-----")
from time import sleep
print ("Deleting in 10 sec")
sleep(10)
os.remove(mypath)