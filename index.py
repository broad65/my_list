##Create an empty list called my_list.
my_list = []
print(my_list)

##Append the following elements to my_list: 10, 20, 30, 40.
my_list = []
print("Before Append:", my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Append:", my_list)

##Insert the value 15 at the second position in the list.
my_list = [10, 20, 30, 40]
my_list.insert(1, 15) 

##Extend my_list with another list: [50, 60, 70]
my_list = [10, 15, 30, 40]
print("list1:", my_list)

shoes_types = ["Boots", "Sandals", "Loafers", "Sneakers"]
print("list2:", shoes_types)
my_list.extend(shoes_types)

print("list after append:", my_list)

##Remove the last element from my_list.

##Sort my_list in ascending order.
##Find and print the index of the value 30 in my_list.