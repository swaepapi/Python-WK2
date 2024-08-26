# Create a list
my_list = []

# Add values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending :", my_list)

# Insert a value
my_list.insert(1, 15)
print( "List after inserting 15 :",my_list)

# Extending list
my_list.extend([50, 60, 70])
print("List after extending :", my_list)

# Removing last element
my_list.pop()
print("List after removing the last element:", my_list)

# Ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)

# Index of the value 30 
index_of_30 = my_list.index(30)
print("The index of value 30  is:", index_of_30)


# The index of value 30 = 3