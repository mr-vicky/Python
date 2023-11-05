A = {1, 2, 3, 4, 5}
B = {10, 20, 30}

# Adding Elements -->
# add() ->
A.add(100)
print(A)

# copy() ->
C = A.copy()
print(C)

# update() -> to add more then one value, can add iterables also
A.update([11, 22, 33])
print(A)
A.update("python")
print(A)
A.update((99, 999, 9999))
print(A)

# Deleting Elements -->
A = {1, 2, 3, 4, 5}

# pop() -> removes element
A.pop()
print(A)
A.pop()
print(A)

# discard() ->
A.discard(5)
print(A)
A.discard(100) # it will not give an ERROR

# remove() ->
A.remove(3)
print(A)
# A.remove(100) # it will give an ERROR

# clear() ->
A = {1, 2, 3, 4, 5}
print(A)
A.clear()
print(A) 