import re

def splitfunction(m):
    word ='_' + m.group()[0].lower() + m.group()[1:]
    return word


file=open("row.txt", "r", encoding="utf8")

pattern=re.compile(r"\B[A-ZА-Я][a-zа-я]*")
print(pattern.sub(splitfunction, file.read()))
