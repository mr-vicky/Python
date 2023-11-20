# operators on String

# 1. Concatination (+) ----->
# s1 = "Hello"
# s2 = "World"
# s3 = s1 + s2
# print(s3)

# s3 = "Vivek" "Sarade"
# print(s3)

# s3 = "Hello" + str(15)
# print(s3)

# s3 = "How " + "are " + "you!"
# print(s3)

# 2. Repetition (*) --->

# s = "I love Python "*100
# print(s)

# 3. Indexing --->

#     0 1 2 3 4
# s =    "Vivek"
# #    -5-4-3-2-1

# print(s[-5], s[0])
# print(s[-4], s[1])
# print(s[-3], s[2])

# for i in range(4, -1, -1):
#     print(s[i])

# 4. Slicing -->
# Syntax: string_name[start:end:step]

# s = "Vicky"
# print(s[0:len(s):1])
# print(s[0::1])
# print(s[::1])
# print(s[:len(s):])
# print(s[::])
# print(s[-1:-len(s)-1:-1])
# print(s[-1::-1])
# print(s[-1::-2])

# 5. 'in' operator -->
s = "Vicky"

print('V' in s)
print('cky' in s)
print('Z' in s)

print('\r')
# 6. 'not in' operator -->
s = "Vicky"

print('V' not in s)
print('cky' not in s)
print('Z' not in s)
