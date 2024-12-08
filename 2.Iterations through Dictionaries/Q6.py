# Iterate through the dictionary student and print all keys.
student = {
    "Name" : "Haseeb",
    "Age" : 17,
    "Grade" : "A",
    "City" : "Fsd"
}
i = 1
print("Student :",student)
for key in student.keys():
    print("key",i," :", key)
    i += 1