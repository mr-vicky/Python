# global variable
g = 100

def fun1(a, b):
    c = a + b # local variables
    print("local", c)
    print("global", g)
    print("locals():", locals()) # locals(): method that returns all the local variables

fun1(10, 20)
print("globals():", globals()) # gloabal(): method that returns all the gloabal variables