def add1(a, b, c, d, e, f):
    return a + b + c + d + e + f

# before / symbol all the arguments must be positional arguments
def add2(a, b, /, c, d, e, f):
    return a + b + c + d + e + f

# after the * symbol all the arguments must be keyword arguments
def add3(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f
# all the arguments in between can be of any type (positional or keyword) 

print(add1(1, 2, 3, 4, 5, 6))
print(add2(1, 2, d=4, c=3, f=6, e=5))
print(add3(1, 2, 3, 4, f=6, e=5))
