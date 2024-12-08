# Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.
dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7 }
dict3 = {}
for k1,v1 in dict1.items():
    for k2,v2 in dict2.items():
        if k1 == k2:
            dict3[k1] = dict1[k1] + dict2[k2]
print(dict3)