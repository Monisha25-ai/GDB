# now main topic list

items = ["apple", "banana", "cherry"]

# Basic list operations
print(items)
print(items[0])  # Accessing the first item 
print(items[-1])  # Accessing the last item
print(items[1:3])  # Slicing the list from index 1 to 2
print(items[1:])  # Slicing from index 1 to the end
print(items[-1:])  # Slicing from the last item to the end

items = ["apple", "banana", "cherry"]

# now methods of list operations
items.append("orange")  # Adding an item to the end
print(items)
items.insert(1, "mango")  # Inserting an item at a specific index
print(items)
items.remove("banana")  # Removing an item by value
print(items)
popped_item = items.pop(1)  # Removing an item by index
print(popped_item)  # This will print the removed item
del items[0]  # Deleting an item by index
print(items)

# Difference between del, pop and remove
# del removes an item by index, pop removes and returns an item by index, and remove removes an item by value.