# String Methods
# s = "Vivek"
# print(dir(str)) # To see all the methods of the class 'str'
# print("\r")


# print(dir(int))0
# print("\r")
# print(help(s.encode))


# find() ->  
# s = "I love python"
# print(s.find('p'))
# print(s.find('o', 5)) # Searches from index 5 to end


# rfind() ->
# print(s.rfind("love")) # searches in reverse order, from end
# print(s.find("Me")) # return -1, if the string doesn't exists


# index() -> 
# print("\r")
# print(s.index("o"))


# rindex() -> 
# print("\r")
# print(s.rindex("o"))
# index() method return an error if the string or character dosen't exist 
# print(s.index("Me")) 


# count() -> 
# print("\r")
# print(s.count('o'))


# ljust(), rjust(), center()  ->  Used to add spaces or character
# s = "Vivek"

# print(s.ljust(20))
# print(s.ljust(20, '*'))

# print(s.rjust(20))
# print(s.rjust(20, '*'))

# print(s.center(10))
# print(s.center(20, '*'))


# lstrip(), rstrip(), strip() --> removes the spaces or characters 
# s = " Vivek  "

# print(s.rstrip())
# print(s.strip())

# s = "+++---Vivek---+++"

# print(s.strip('+'))
# print(s.strip("+-")) 


# capitalize(), lower(), upper(), title(), swapcase(), casefold() ---->
# s = "i loVe python"
# print(s)
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.casefold()) # converts to lower case but recommeded to use instead of lower(), for other languages, Ex- German, etc


# isupper(), islower(), istitle(), isalnum(), isalpha(), isspace(), isascii() --->
# s = "Vivek"
# print(s.isupper())
# print(s.islower())
# print(s.istitle())
# print()

# s = "Vivek123"
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isascii())

# s = "    "
# print(s.isspace())


# isidentifier(), isprintable() ->
# s = "result"
# print(s.isidentifier())

# s = "123@result"
# print(s.isidentifier())

# s = "I love Python"
# print(s.isprintable())

# s = "I love python\n"
# print(s.isprintable())


# isdecimal(), isnumeric(), isdigit() -->
# s = "124"
# print(s.isdecimal())
# print(s.isdigit())
# print(s.isnumeric())

# s = "12.3"
# print(s.isdecimal())
# print(s.isdigit())
# print(s.isnumeric())
