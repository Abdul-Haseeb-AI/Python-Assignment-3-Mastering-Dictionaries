# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
dict = {'a': 10, 'b': 15,'c': 10, 'd': 15}
def checkValue(key):
    if key:
        return dict[key]
    else:
        print("Key not found")
keyName = input("Key :")
print(checkValue(keyName))