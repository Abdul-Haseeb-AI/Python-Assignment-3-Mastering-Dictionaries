#Check if the key grade exists in the student dictionary and print True or False. 
student = {
    "Name" : "Haseeb",
    "Age" : 17,
    "Grade" : "A",
    "City" : "Fsd"
}
print("Student :",student)
if "Grade" in student:
    print(True)
else :
    print(False)