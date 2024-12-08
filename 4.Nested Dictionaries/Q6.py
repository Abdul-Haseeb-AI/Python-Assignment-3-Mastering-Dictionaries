# Nested Dictionaries
# Create a nested dictionary to represent the following data:
#Person:  
#  Name: John  
#  Age: 30  
#  Address:  
#    Street: 123 Elm St  
#    City: Boston  
person = {
        "Name" : "John",
        "Age" : 30,
        "Address" : { 
           "Street" : "123 Elm St",  
           "City" : "Boston"
            }
          }

print("Person Dictionary : ", person)