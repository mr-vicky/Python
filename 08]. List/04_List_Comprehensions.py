L1 = [x for x in range(10)]

print(L1)

L2 = [x**2 for x in range(1, 10)]
print(L2)

l3 = [x for x in range(100, 200)]
# print(l3)

l4 = [x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) if x%2 == 0]
print(l4)

l5 = [x.capitalize() for x in "Python"]
print(l5)

l6 = [x for x in "eiuufasf&YRYQ(RIU#(*{98394u3}sgs)fwf)af" if x.isalnum()]
print(l6)


# Creating a list of names : 
# Method 1
data = input("Names: ")
ListNames = data.split()
print(ListNames)

# Method 2
ListNames2 = input("Names: ").split()
print(ListNames2)