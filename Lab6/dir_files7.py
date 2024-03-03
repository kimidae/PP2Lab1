file=open("file.txt", "r")
sum=0
list_of_strings=[]
for x in file:
    list_of_strings.append(x)
file.close()
file = open("file_COPY.txt", "w")
for x in list_of_strings:
    file.write(x)