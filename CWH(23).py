# List Methods

l1 = [1,2,3,4,6]
l1.append(7) #adds element at end
print(l1)

l2 = [1,8,7,25,48,3,71]
l2.sort() #arrange the list in ascending order
print(l2)

l3 = [8,7,6,5,4,3,2,1]
l3.reverse() #reverse the list
print(l3)

l4 = [11,45,1,2,4,6]
print(l4.index(4)) #tells the position

l5 = [1,7,5,9,4,1,1,6,7]
print(l5.count(1)) #counts the element in list

l6 = [4,8,12,16,20]
l6.insert(1, 6)
print(l6) #adds the element in specific position

l7 = [900,1000,1100]
l1.extend(l7)
print(l1) #adds the another list at the end