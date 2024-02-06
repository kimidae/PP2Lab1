'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
'''

''''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
'''

'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
'''

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
'''

'''

'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)