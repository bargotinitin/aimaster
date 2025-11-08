
# List items are ordered, changeable, and allow duplicate values.

list1 = ["Super Heroes", "Spiderman", 98, 878, 89.90]

print(len(list1))

print(list1)
print(list1[1:2])
print (list1[1])
print (list1[2])

list1[0] = "Ironman"
print (list1)

list1.append("Captain America")
print (list1)


list1.insert(4, "Doctor Strange")
print (list1)

list1.pop(3)
print (list1)

list1.remove(89.90)
list1.remove(98)
print (list1)


# del list1
# print (list1) # list will not exist after delete

# list1.clear()
# print (list1) # list will exist after clear

for x in list1:
 print (x)

list1.sort() # Default ASC
print(list1)

list1.sort(reverse = True)
print(list1) # Sorts in DESC order

list2 = list1.copy()
print(list2)

list3 = ["Black Widow", "Doctor Banner", "Hawk Eye"]
list4 = list1 + list3
print(list4)

list2.extend(list3)
print(list2)


