def has_33(nums):
    c=0
    for x in nums:
        if (c == 3 and x == 3) :
            return True
        c = x
    return False
    

if (has_33(nums = [1, 3, 3])):
    print ("True")
else:
    print ("False")
if(has_33(nums = [1, 3, 1, 3])):
    print ("True")
else:
    print ("False")
if (has_33(nums = [3, 1, 3])):
    print ("True")
else:
    print ("False")