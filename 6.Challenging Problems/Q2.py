# Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
dict = {}
n= int(input("Enter Dictionary Length :"))
for i in range(n):
    key = int(input("Enter Key :"))
    dict[key] = key ** 3
print("Required Dictionary : ",dict)