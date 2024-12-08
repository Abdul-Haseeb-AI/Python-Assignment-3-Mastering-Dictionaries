# Add a new key Phone to the nested dictionary with the value "123-456-7890".
Class = {
    "st1" : {
        "Roll no." : 1,
        "Name" : "Ali"
      },
    "st2" : {
        "Roll no." : 2,
        "Name" : "Ahmad"
      }
  }
print(Class)
Class["st1"]["Phone"] = "123-456-7890"
print("Updated Dictionary :",Class)