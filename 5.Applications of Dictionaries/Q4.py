# Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}
dict = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
stack = {}
for key,val in dict.items():
    if dict[key] not in stack.values():
        stack[key]=val  
print(f"dictionary : {stack}")