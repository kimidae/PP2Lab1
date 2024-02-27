import re

file=open("row.txt", "r", encoding="utf8")
mylist=[]
for row in file:
    mylist+=re.findall("ab*", row)
print (mylist)