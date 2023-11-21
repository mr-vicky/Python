
file = open('prop.txt', 'r')

# Properties -->
print(file.name)
print(file.mode)
print(file.closed)

# methods -->
# content1 = file.read() # reads all the content from the file
# print(content1)

# content2 = file.readline() # reads one line at a time
# print(content2)

content3 = file.readlines() # reads multiple lines 
print(content3)
file.close()