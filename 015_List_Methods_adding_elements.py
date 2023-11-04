# l1 = [1,2,3]
# print(l1)

# # append() ---->
# l1.append(4)
# print(l1)

# # extend() ---->
# l1.extend([5,6,7])
# print(l1)

# # insert(i, x)
# l1.insert(0, 10)
# print(l1)

# # copy() ---->
# l2 = l1.copy()
# print(l2)

# pop() --->
l3 = [1,2,3,4,5,6,7,8,9,10]

# l3.pop()
# print(l3)

# l3.pop(0)
# print(l3)

# # delete() --->
# del l3[0]
# print(l3)

# remove() --->
l3 = [1,2,3,4,5,6,7,8,9,10]

l3.remove(6)
# print(l3)

# clear() --->
l3.clear()
# print(l3)


# index(value[, start[, end[]]) --->
l1 = [2,3,4,5,6,2,4,6,7,8,9,0]

# print(l1.index(2))
# print(l1.index(2, 2))
# print(l1.index(2, 2, 5)) # if element not found returns error

# count() --->
print(l1.count(6))

# reverse() --->
l1.reverse()
print(l1)

# sort(*, key=none, reverse=false) ---> This function modifies the string
l1.sort()
print(l1)

l2 = ["zz", "bb", "AA", "EE", "nn", "JJ"]

l2.sort()
print(l2)

l2.sort(key=str.lower)
print(l2)

# sorted() ---> This function does not modify the string 
print(sorted(l2))