# Delete the Address key from the nested dictionary.  
person = {
        "Name" : "John",
        "Age" : 30,
        "Address" : { 
           "Street" : "123 Elm St",  
           "City" : "Boston"
            }
          }
print("Dictionary : ", person)
del person["Address"]
print("Updated Dictionary : ", person)