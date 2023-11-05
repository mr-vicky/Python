t1 = ("Mr Vicky", 3+4j, 99, 200.89)

print(t1)

for x in t1:
    print(x)

print("\n")
for i in range(len(t1)):
    print(t1[i])

print("\n")
i = 0
while i < len(t1):
    print(t1[i],  end=' ')
    i+=1

# index ->
print(t1[0])

# slice ->
print(t1[:])

# concatinate ->
t2 = 10, 20, 30, 40, 50
print(t2 + t2)

# Repeat ->
print(t1*5)

# Membership(in, not in)
print(10 in t2)
print(100 in t2)
print(100 not in t2)