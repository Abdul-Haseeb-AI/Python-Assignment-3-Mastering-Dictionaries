# Delete the Address key from the nested dictionary.  
person = {
        "Name" : "John",
        "Age" : 30,
        "Address" : { 
           "Street" : "123 Elm St",  
           "City" : "Boston"
            }
          }
i = 1
for key in person.keys():
    print(f"key {i} : {key}")
    i += 1