myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(myList[:])
# print(myList[0:10:1])
# print(myList[4:])

# print(myList[2:6:])

# print(myList[7::1])

# print(myList[0::3])

# print(myList[::-1])

# print(myList[-1:-11:-1])


# List can be modified using slicing ----->
myList[0:5:1] = {100, 200, 300}

print(myList)

# Concatination of Lists ---->

list1 = [1,2,3,4]
list2 = [10,20,30]

list3 = list1 + list2

print(list3)

# extend() Method : 
list3.extend([100,200,300])
print(list3)

# * Operations ----->

list1 = [1,2,3]

print(list1*3)

if 1 in list1:
    print("Found")
else:
    print("Not Found")

print(1 in list1)
print(10 in list1)
print(10 not in list1)

# Traversing the List --->

for x in list1:
    print(x)

for i in range(0, len(list1)):
    print(list1[i])

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

