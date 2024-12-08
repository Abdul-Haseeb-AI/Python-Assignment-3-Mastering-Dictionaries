# Iterate through the dictionary student and print all key-value pairs in the format key: value.
student = {
    "Name" : "Haseeb",
    "Age" : 17,
    "Grade" : "A",
    "City" : "Fsd"
}
print("Student :",student)
for key,val in student.items():
    print(f"{key} : {val}")