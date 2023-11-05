t1 = tuple(x for x in range(0, 10))
print(t1)

t2 = tuple(x for x in range(0, 10, 2))
print(t2)

t3 = tuple(x for x in "MrVicky" if(x.lower()))
print(t3)

# Tuple Methods ->
t4 = 1, 2, 2, 2, 4, 5, 6, 6, 6, 6
print(t4)
# count() -->
print(t4.count(6))
print(t4.count(2))
# lower() -->
print(t4.index(1))