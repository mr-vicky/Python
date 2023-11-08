def add(a, b=0, c=0):
    return a + b + c

print(add(1, 2, 4))
print(add(1, 2))
print(add(1))

# Ex-2
def addItem(item, list=[]):
    list.append(item)
    return list

List = [1, 2, 3, 4, 5]
print(addItem(6, List))
# it maintains the seperate empty list for only item as a argument
print(addItem(12))
print(addItem(13))
print(addItem(14))