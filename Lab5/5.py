import re

def findbypattern(row):
    pattern = r'a\w*b'
    sequences = re.findall(pattern, row)
    return sequences

file=open("row.txt", "r", encoding="utf8")
mylist=[]
for row in file:
    mylist+=findbypattern(row)
print (mylist)