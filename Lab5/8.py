import re

def splitfunction(row):
    return re.split("[А-ЯA-Z]", row)

file=open("row.txt", "r", encoding="utf8")
mylist=[]
for row in file:
    print(splitfunction(row))