S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

# Union 
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)

# Symmetric Difference 
print(A ^ B)
    
# issubset and proper subset
print(A < S) # A is subset of S
print(A <= S)

# issuperset
print(S > A)
print(S >= A)

# is Equal Sets
print(S == S)

# is Un-Equal Sets
print(A != B)

# in 
print(10 in S)
print(100 in S)

# not in
print(100 not in S)
print(10 not in S)