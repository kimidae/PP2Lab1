def histogram(num):
    for x in num:
        for i in range (x):
            print ("*", end="")
        print(end = "\n")

num = [1, 2, 5, 28]
histogram(num)