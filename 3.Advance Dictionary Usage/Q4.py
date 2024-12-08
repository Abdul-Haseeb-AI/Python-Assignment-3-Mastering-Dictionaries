# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
dict = {'a': 1, 'b': 2, 'c': 3} 
newDict = {}
for val,key in dict.items():
    newDict[key] = val
print(f"Reversed Dictionary : {newDict}")