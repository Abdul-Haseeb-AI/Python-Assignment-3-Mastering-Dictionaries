# Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
dict = {'a': 10, 'b': 15, 'c': 7}
max = 0
for key,val in dict.items():
    if dict[key] > max:
        keyName = key
        max = dict[key]
print(f"dict[{keyName}] : {max}")f"dict[{keyName}] : {max}")