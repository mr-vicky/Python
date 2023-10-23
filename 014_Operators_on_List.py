myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(myList[:])
print(myList[0:10:1])
print(myList[4:])

print(myList[2:6:])

print(myList[7::1])

print(myList[0::3])

print(myList[::-1])

print(myList[-1:-11:-1])


# List can be modified using slicing
myList[0:5:1] = {100, 200, 300}

print(myList)