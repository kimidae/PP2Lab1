import re

def changefunction(row):
    partofstr=row.split('_')
    sequences = partofstr[0] + ''.join(x.title() for x in partofstr[1:])
    return sequences

file=open("row.txt", "r", encoding="utf8")
mylist=[]
for row in file:
    print(changefunction(row))