def rev(substr):
    substr = substr[::-1]
    print (substr, end = " ")
    
str = "We are ready"
substr=""
for x in range (len(str)-1, -1, -1):
    if str[x]!=" ":
        substr+=str[x]
    if str[x]==" ":
        rev(substr)
        substr=""
rev(substr)