# Variable length arguments
def fun1(*args):
    print(args)

print(10)
print(10, 20, 30)
print(10, 20, 30, 40, 50)

# Keyword variable length arguments
def fun2(**kwargs):
    for x in kwargs:
        print(x, kwargs[x])

fun2(name="MrVicky", roll_no =96, address="Maharashtra")