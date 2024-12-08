# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
dict = {}
for val in range(1,6):
    dict[val]=val*val
print(f"dictionary : {dict}")