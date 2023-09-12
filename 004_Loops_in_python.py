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
i = 1
while(i <= 10):
    if(i % 2 == 0):
        pass
    else:
        print(i)
    i += 1