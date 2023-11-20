# S = {expression for item in iterable}

S = {} # this will not create an empty set, it will create empty dict
print(type(S))
# use set() to create empty set
S1 = set()
print(S1)
print(type(S1))

S2 = {x for x in range(10)}
print(S2)

S3 = {x**2 for x in [1, 2, 3, 4, 5, 6]}
print(S3)

S4 = {x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9,) if(x%2 == 0)}
print(S4)

S5 = {x.upper() for x in "philippines"}
print(S5)