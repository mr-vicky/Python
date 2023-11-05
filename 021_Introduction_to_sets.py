# Set is the collection of HETEROGENEOUS objects
s = {1, 2.3, 3+4j, "five"}
print(s)

# Unordered
# print(s[0]) # returns an error

# No Duplicates
s1 = {1, 2, 1, 1, 1, 1, "TWO", "TWO"}
print(s1)

# Growable 
s1.add(100)
s1.add(200)
print(s1)

# deleting value
s1.discard("TWO")
print(s1)

print(len(s))

s2 = {5, 10, 21, 15, 3, 11 }
print(s2)
