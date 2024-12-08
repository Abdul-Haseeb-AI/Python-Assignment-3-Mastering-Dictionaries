# Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {}
for key,val in dict1.items():
    if val > 3:
        dict2[key] = val
print("Dictionary :",dict2)