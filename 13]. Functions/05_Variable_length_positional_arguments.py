# Variable length arguments --->
def fun1(*args):
    print(type(args), args)

fun1()
fun1(1, 2)
fun1(1, 2, 3, 4, 5, 6)
fun1(11, 22, 33, 44, 55, 66, 77, 88, 99)
print()

# Unpacking arguments --->
def fun2(a, b, c):
    print(a, b, c)

list = [100, 200, 300]
fun2(*list)

str = "ZIP"
fun2(*str)

mySet = {12, 23, 34}
fun2(*mySet)
print()

# Multiple return values --->
def fun3(a, b, c):
    return a**2, b**2, c**3

a, b, c = fun3(1, 2, 3) # we can store them in seperate variables
print(a, b, c)

t = fun3(1, 2, 3) # also we can store them in a single variable which will form a tuple
print(t, type(t))