# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
def check(d1,d2):
    if sorted(d1) == sorted(d2):
        return True
dict1 = {'a': 1, 'b': 2, 'c': 3} 
dict2 = { 'b': 2, 'c': 3,'a': 1} 
if check(dict1,dict2) == True:
    print("Identical Dictionaries")
else:
    print("Nonidentical Dictionaries")