t1 = (1, 2, 3, 4, 5)

print(t1)
print(type(t1))

# function to create a tuple
t2 = tuple(("One", 2.3, 2000, "Four", 2000 ))
print(t2)

# Tuple is Immutable -->
# t2[5] = 10 
print(t2)

t3 = ()
print(t3)

t4 = (100) # this is not a tuple its an integer variable
print(t4)
print(type(t4))

# To create tuple with one value we must add a coma(,)
t5 = (100,)
print(t5)
print(type(t5))

# Packing and Unpacking
# Packing ->
t6 = 1, 2, 3, 4, 5
print(t6)

# Unpacking ->
a, b, c, d, e = t6
print(a)
print(b)
print(c)
print(d)
print(e)

# Crating a tuple by passing list
list = [100, 200, 300, 400]
t7 = tuple(list)
print(t7)

# Creating a tuple by passing string
str = "python"
t8 = tuple(str)
print(t8)

# Packing can be done only in Tuple
t9 = "Vivek", "Nitesh", "Sanket", "Prathamesh", "Prasad"
print(t9)

# Unpacking can be done in List, String and Tuple
a, b, c = "SKY"
print(a, b, c)

List2 = [11, 22, 33]
x, y, z = List2
print(x, y, z)