Dict1 = dict({"apple": "red",
              "mango": "yellow",
              "orange": "orange" 
              })


# copy() ->
Dict2 = Dict1.copy() # This will create a shallow copy of Dict1 and store that in Dict2
print(Dict1)
print(Dict2)
print(id(Dict1["apple"]))
print(id(Dict2["apple"]))

# update() ->
Dict3 = {1: "apple", 2: "Mango", 3: "Orange", 4: "Watermelon"}
Dict4 = {5: "Kiwi", 6: "Cherry"}

Dict3.update(Dict4)
print(Dict3)

# setdefault() ->
Dict3 = {1: "apple", 2: "Mango", 3: "Orange", 4: "Watermelon"}
print(Dict3.setdefault(1))

print(Dict3.setdefault(10)) # if the key is not present then it will add the key and set None as its value
print(Dict3)

print(Dict3.setdefault(11, "adv"))
print(Dict3)

# fromkeys() ->
Dict4 = {}
list = [1,2,3,4,5]
thisDict = Dict4.fromkeys(list, False)
print(thisDict)

# pop() ->
print(thisDict)

thisDict.pop(1)
print(thisDict)
print(thisDict.pop(100, "Not found"))

# popitem() -> removes the last element
print(thisDict)
thisDict.popitem()
print(thisDict)

# clear() -> removes all the elements 
print(thisDict)
thisDict.clear()
print(thisDict)