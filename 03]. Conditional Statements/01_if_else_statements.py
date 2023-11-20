print("If else statements -->")
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Negative")

# If else with logical operators
print("If else with logical operators -->")
a = 10
b = 20
c = 30

# and operator: 
if a < b and a < c: 
    print("a is the smallest")
else:
    print("a is not the smallest")

# or operator: 
if a < 0 or a == 0: 
    print("a is less that or equalzero")
else:
    print("a is not less that or equal zero")

# Nested elif
print("nested elif--> ")
a1 = 20
a2 = 21
a3 = 21

if a1 < a2 and a1 < a3:
    print("a1 is smallest")
elif a2 < a1 and a2 < a3:
    print("a2 is smallest")
else:
    print("a3 is smallest")