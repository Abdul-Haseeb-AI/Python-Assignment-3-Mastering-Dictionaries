# Flatten the following nested dictionary into a single-level dictionary:
givenDict={'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
stack = {}
def flat_dict(givenDict):
    for key,val in givenDict.items():
        if isinstance(val,dict):
            flat_dict(val)
        else:
            stack[key] = val
flat_dict(givenDict)
print("Flatten Dictionary",stack)