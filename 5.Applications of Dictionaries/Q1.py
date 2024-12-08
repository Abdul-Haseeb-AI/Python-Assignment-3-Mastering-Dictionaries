# Use a dictionary to count the occurrences of each word in the string "hello world hello python world".
str = "hello world hello python world"
str = str.split()
dict = {}
for word in str:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1
print("Dictionary",dict)