Dict1 = {"name" : "Vicky",
         "Branch": "Computer Science",
         "Contact": 9090909090}
print(Dict1) 

Dict2 = dict({"Good": "Bad",
             "Fast": "Slow",
             "Top": "Down"})
print(Dict2)

# Accessing the values using keys
print(Dict1["name"])
print(Dict1["Branch"])
print(Dict1["Contact"])

# Updating the values
Dict1["name"] = "Mr Vicky"
print(Dict1["name"])

# Deleting the key-value pair
print(Dict1)
del Dict1["name"]
print(Dict1)