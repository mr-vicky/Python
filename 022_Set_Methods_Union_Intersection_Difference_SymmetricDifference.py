A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

# union() ->
print(A.union(B))

# intersection() ->
print(A.intersection(B)) # create a new set to store result
print(A.intersection_update(B)) # store the result in A (updates the set A)

# difference ->
print(A.difference(B)) # create a new set to store result
print(A.difference_update(B)) # stores the result in A (updates the set A)
print(B.difference(A))

# symmetric differnce 0>
print(A.symmetric_difference(B)) # create a new set to store result
print(A.symmetric_difference_update(B)) # stores the result in A (updates the set A)

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
C = {1, 2, 3}

# issubset ->
print(C.issubset(A))

# issuperset() ->
print(A.issuperset(C))

# isdisjoint() ->
print(B.isdisjoint(C))

print(dir(set))