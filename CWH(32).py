# Set Methods

# Union & Update Method
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1)

# Intersection Method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Vishakapatnam","Mumbai","Delhi","Pune"}
print(cities1.intersection(cities2))

# Symmetric Difference Method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Vishakapatnam","Mumbai","Delhi","Pune"}
print(cities1.symmetric_difference(cities2))

# Difference Method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Vishakapatnam","Mumbai","Delhi","Pune"}
print(cities1.difference(cities2))

# isdisjoint method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Vishakapatnam","Mumbai","Delhi","Pune"}
print(cities1.isdisjoint(cities2))
# True if both sets does not have any common value

# issuperset method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Kolkata","Delhi"}
print(cities1.issuperset(cities2))
cities3 = {"Mumbai","Chennai","Pune"}
print(cities1.issuperset(cities3))
# True if set1 has values present in set2

# issubset method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities2 = {"Kolkata","Delhi"}
cities3 = {"Mumbai","Chennai","Pune"}
print(cities3.issubset(cities1))
# vice-versa of insuperset method

# add method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities1.add("Kolkata")
print(cities1)
# Adds element in the set.
# different from update method because add is used to add only element

# Remove/Discard method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities1.remove("Pune")
print(cities1)
# if element is absent in set discard will not raise error

# pop method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
item = cities1.pop()
print(cities1)
print(item)

# del keyword
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
# del cities1
print(cities1)
# delets element in set

# clear method
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
cities1.clear()
print(cities1)

# to check whether the item is present or not
cities1 = {"Pune","Banglore","Mumbai","Chennai"}
if "Pune" in cities1:
    print("Pune is present")
else:
    print("Not Found")

