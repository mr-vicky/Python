# 1. Sorting letters of a string ->
# s = "fvuibawwdqwofvor"
# ss = sorted(s)
# print(ss)

# str2 = ''.join(ss)
# print(str2)

# Challenge 2: Bill receipt format item_name.........price within size of 25 characters --->
# item = input("Enter Item name: ")
# price = input("Enter Price: ")

# total_length = len(item) + len(price)

# dots = '.'*(25-total_length)

# print(item + dots + price)


# Challenge 3: Validating the Passwords ------------->

# pass1 = input("Enter the password: ")

# pass2 = input("Enter the password again: ")

# if(pass1 == pass2):
#     print("Password is correct...")
# elif(pass1.capitalize() == pass2.capitalize()):
#     print("Check the cases properly...!")
# else:
#     print("Invalid Password...!")
    
# Challenge 4: Credit Card Details ---------->

# card_no = input("Enter the Credit card Number: ")

# hide = '*'*4 + ' '
# print(hide*3 + card_no[15:])


# Challenge 5: Domain Name form Email ------------->
# email = input("Enter Email ID: ")

# aIndex = email.find('@')

# print("Username: ", email[:aIndex])
# print("Domain: ", email[aIndex+1:])

# Challenge 6: Check for Palindrome if its not a palindrome make it palindrome ---------->
# str1 = input("Enter a string: ")
# str2 = str1[::-1]

# if(str1 == str2):
#     print("Its a plindrome: ", str1)
# else:
#     print(str1 + str2)

# Challenge 7: Find the Day, Month and the Year -------->
# date = input("Enter the Date in format DD/MM/YYYY : ")

# l = date.split("/")

# print("Day:", l[0])
# print("Month:", l[1])
# print("Year:", l[2])


# Challenge 8: Check for Anagram ------>

# str1 = input("Enter the str1: ")
# str2 = input("Enter the str2: ")

# str1 = sorted(str1)
# str2 = sorted(str2)

# if (str1 == str2):
#     print("Anagram")
# else:
#     print("Not an Anagram")
# print(str1)
# print(str2)


# Challenge 9: Rearranging the cases ------->
# s = input("Enter the string: ")

# low = ""
# up = ""

# for x in s:
#     if x.islower():
#         low = low + x
#     else:
#         up = up + x

# print(low + up)


# Challenge 10: Remove Punctuations -------->
s = input("Enter the Email ID: ")

s1 = ""

for x in s:
    if x.isalnum():
        s1 += x

print(s1)