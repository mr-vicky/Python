# ITERATORS --->
L = {1, 2, 4, 5, 6, 7, 8, 9, 10}

it = iter(L)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # this will give an error as the iteraor is on last element
print("\n")


# GENERATORS --->
# Generators : We can say that it is an another way of creating our own iterators by using keyword 'yeild' instead of return.
def days():
    L = ["Sun", "Mon", "Tue", "Wedn", "Thus", "Fri", "Sat"]
    i = 0
    while(True):
        x = L[i]
        i = (i + 1) % 7
        yield x
    
d = days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))