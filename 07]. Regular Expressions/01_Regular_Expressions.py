import re

pattern = r"Python"
res = re.match(pattern, "Python is a language")

print(res.group())
  
pattern = r"a+"
res = re.match(pattern, "aaaaaaaaaaaaaaab")
print(res.group()) 