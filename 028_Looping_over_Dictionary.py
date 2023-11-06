Dict1 = {101: "Vivek",
         102: "Prasad",
         103: "Nitesh",
         104: "Sanket",
         105: "Prathamesh"
         }

print(Dict1[101])
print(Dict1.get(101))


# print(Dict1[109]) # this will throw an ERROR
print(Dict1.get(109)) # this will not throw an error
print(Dict1.get(109, "Not found the key"))
print()


# keys()
print(Dict1.keys())
print()

for k in Dict1.keys():
    print(k, Dict1[k])
print()


# values()
print(Dict1.values())
print()

for v in Dict1.values():
    print(v)
print()


# items()
print(Dict1.items())
print()

for x,y in Dict1.items():
    print(x, y)
print()