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


# # isdecimal(), isnumeric(), isdigit() -->
# s = "124"
# print(s.isdecimal())
# print(s.isdigit())
# print(s.isnumeric())

# s = "12.3"
# print(s.isdecimal())
# print(s.isdigit())
# print(s.isnumeric())

# # startswith(), endswith(), removesuffix(), removeprefix(), partition(), rpartition() --->
# s = "python is very easy"

# # startswith() -->
# print(s.startswith("python"))
# print(s.startswith("py"))

# print(s.startswith("is"))
# print(s.startswith("is", 7)) # starting index 7


# # endswith() -->
# print(s.endswith("easy"))
# print(s.endswith("is"))
# print(s.endswith("is", 0, 9))

# s = "vivek@gmail.com"

# print(s.endswith("@gmail.com")) # can be used for email validation

# # removesuffix() -->
# s = "python programming"

# print(s.removesuffix("ing"))
# print(s.removesuffix("programming"))


# # removeprefix() -->
# print(s.removeprefix("python"))
# print(s.removeprefix("py"))

# # partition() --> 
# s = "python is very easy"

# print(s.partition(("is")))
# print(s.partition("s"))
# print(s.rpartition("s")) # partition form R.H.S

# # replace(), join(), split(), rsplit(), splitlines() ---> 

# # replace() -->
# s = "viveksarade@gmail.com"

# print(s.replace("gmail", "yahoo"))

# s = "v-i-v-e-k"
# print(s.replace('-', ''))

# you can remove any character or space from every program or text for example ->
# # Example 1 ->
# s = '''print("Hello World!");
#       this is a python program after removing semicolons; '''
# print(s)
# print("\r")
# print(s.replace(';', ''))

# # Example 2 -> Removing the spaces from the following paragraph
# s = '''This Python Tutorial is very well suited for Beginners, and also for experienced programmers with other programming languages like C++ and Java. This specially designed Python tutorial will help you learn Python Programming Language in the most efficient way, with topics from basics to advanced (like Web-scraping, Django, Deep-Learning, etc.)'''

# print(s)
# print("\r")
# print(s.replace(' ', '')) # remove spaces

# # join()-->

# s1 = "ABCDE"
# s2 = '-'
# print(s2.join(s1))

# list1 = ["Python", "C", "C++"]
# s = "   "
# print(s.join(list1))

# # split() -->
# s = "I love python"
# print(s.split())

# s = "I-love-python"
# print(s.split())
# print(s.split('-'))
# print(s.split('-', 1))
# print(s.rsplit('-', 1))

# # splitlines() -->
s = "aaa\nbbb\tccc\rddd\n"
print(s.splitlines())
print(s.splitlines(keepends = True))

print(s.split()) 