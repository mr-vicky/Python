# Variables
a = 1925
Name, Income, CompanyName = "Mr. Vicky", "1000000000", "Sarade Group"
x = y = z = 1925

print(Name)
print(a)
print(CompanyName)

print(x) 
print(y)
print(z)

# Note -> Python is Dynamically Typed Language
x = 12
print(type(x))
x = 19.25
print(type(x))
x = "String"
print(type(x))

# Variables 

# Numeric Datatypes : int & float ---->
# Note -> The amount of memory taken by any datatype is not fix
a = 12131475758595385849539313831491294394403
print(a)
print(type(a))

# sizeof() function to check the amount of memory consumed by a variable : syntac-> variable_name.__sizeof__()
print(a.__sizeof__())

# Note -> You can represent the value of a variable in a scientific notation also 
decimal = 1925E-2
print(decimal)