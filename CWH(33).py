# Dictionaries in Python
# used to store multiple values in single variable
dic = {
    "Karry" : "Human",
    "Spoon" : "Object"
}

print(dic["Karry"])


# to store roll no.
dic1 = {
    122 : "Karry",
    56 : "Aditya",
    89 : "Mayank",
    13 : "Vinit"
}

print(dic1[56])



info = {"name":"Karan","age":19,"eligible":True}
print(info)



# to print perticular value
info = {"name":"Karan","age":19,"eligible":True}
print(info["name"])
print(info.get("name")) #get can also used to print single value
# get is also used to write error free code



info = {"name":"Karan","age":19,"eligible":True}
# print(info["name"])
print(info.get("name2"))
# instead of error it will show none



# To access multiple value
info = {"name":"Karan","age":19,"eligible":True}
print(info.keys())
print(info.values())



for key in info.keys():
    print(info[key])



print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")