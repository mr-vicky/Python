file = open("myText.txt", "r")
str = file.read(2) # reading the 10 characters from the file
print("\n")
s = file.read(10) # reading the next 10 characters from the file
print(str)
file.close()