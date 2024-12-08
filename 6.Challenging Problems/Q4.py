# Write a Python program to split a dictionary into two based on whether the values are odd or even.
dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
evenDict = {}
oddDict = {}
for key,val in dict.items():
    if val % 2 == 0:
        evenDict[key]=val
    else:
        oddDict[key]=val
print("Dictionary",dict)
print("Even Numbers Dictionary :",evenDict)
print("Odd Numbers Dictionary :",oddDict)