# Iterate through the dictionary student and print all values.
student = {
    "Name" : "Haseeb",
    "Age" : 17,
    "Grade" : "A",
    "City" : "Fsd"
}
i = 1
print("Student :",student)
for val in student.values():
    print("value",i," :", val)
    i += 1