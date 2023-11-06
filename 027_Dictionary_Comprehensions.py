# dict()
Dict1 = dict({"apple": "red",
              "mango": "yellow",
              "orange": "orange" 
              })
print(Dict1)

# empty dictionary
Dict = {}
print(dict)

# zip()
list = [1, 2, 3, 4]
str = "NAIL"
# Dict2 = dict(zip(list, str))
# print(Dict2)

for x in Dict1:
    print(x, Dict1[x])
print()

# get()
for x in Dict1:
    print(x, Dict1.get(x))

print()
Dict2 = {101: "Vivek", 102: "Nitesh", 103: "Sanket", 104:"Prathamesh", 105: "Prasad"}
print(Dict2[101])
print(Dict2.get(101))

print(Dict2[108]) # this will give an error
print

# keys()
print(Dict1.keys())

# values()
print(Dict1.values())

# items()
print(Dict1.items())