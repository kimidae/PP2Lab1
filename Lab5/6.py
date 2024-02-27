import re

def findbypattern(row):
    sequences = re.sub(r"[ ,.]", ":", row)
    return sequences

file=open("row.txt", "r", encoding="utf8")
mylist=[]
for row in file:
    print(findbypattern(row))