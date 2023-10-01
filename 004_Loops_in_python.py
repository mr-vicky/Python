# count = 10
# while count >= 0:
#     print("count")
#     count-=1


# Print the digits of the number ------>
# n = int(input("Enter a number"))
# while n > 0:
#     r = n % 10
#     n //= 10
#     print(r)


# Multiplication Table ------>
# n = int(input("Enter the number: "))
# print("Multiplication table of ", n)
# count = 1
# while count != 11:
#     print(n*count)
#     count += 1


# Infinite Loops ---->
# while (True):
#     n = int(input("Enter the number: "))
#     if(n > 0):
#         print("Positive Number")
#     elif(n < 0):
#         print("Negative Number")
#     else: 
#         break

# pass keyword ---->
# i = 1
# while(i <= 10):
#     if(i % 2 == 0):
#         pass
#     else:
#         print(i)
#     i += 1

# For Loop in Python
# name = "MrVicky"

# for x in name:
#     print(x)

# for i in range(10):
#     print(i)

# print("\n")
# for i in range(25, 31):
#     print(i)

# print("\n")
# for i in range (2, 11, 2):
#     print(i)

# print("\n")
# for j in range (-10, 1, 2):
#     print(j)

# # Challenge Multiplication tabl
# n = int(input("Enter the number: "))

# for i in range(1, 11, 1):
#     print(i, "x", n, "=", i*n)

# Challenge Multiplication tabl
# n = int(input("Enter the number "))
# fact = 1
# for i in range (1, n+1):
#     fact *= i
# print(fact)


# for and else
# for i in range(0,9+1):
#     print(i)
# else:
#     print("For loop is completely executed: ")

# Nested loop ->
# for i in range(0, 5):
#     for j in range(0, 5):
#         print(i, j)


# * Star Pattern -> 
# for i in range(5):
#     for j in range(5):
#         if i <= j:
#             print('*', end = ' ')
#     print('')

# In Python * Star pattern can be done using single for loop also ->
for i in range(6):
    print('* ' * i)