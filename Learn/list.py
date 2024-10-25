# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])

# True or False.
# List items cannot be removed after the list has been created.
thislist = ["apple", "banana", "cherry"]
original_list = thislist.copy()  # Make a copy of the original list
thislist.insert(2, "watermelon")  # Insert "watermelon" at index 2
# Check if the current list is different from the original
if thislist != original_list:
    print("Yes, it's true")
else:
    print("False")