
unsorted_array = ["banana", "apple", "grape", "orange", "pear", "mango", "kiwi", "peach", "plum","cherry"]
print(unsorted_array)
print("Our favourites fruit name is",unsorted_array[5]) # Index count on every string and it's a part of slicing.
print (unsorted_array[9])
print (unsorted_array[3])

# Calculate length
print(len(unsorted_array))

# When you write 1,2,3,4.....like that when we use "for in"
for x in unsorted_array:
    print(x)

# If you want to delete somthing in the array,it's have 2 method 
# pop method its use index wies
unsorted_array.pop(4)
print(unsorted_array)

# remove method it's work value wies
unsorted_array.remove("kiwi")
print(unsorted_array)
    
# Sort the array,we use sorrt() function
unsorted_array.sort()
print(unsorted_array)

# if you add somthing in your array
unsorted_array.append("Coconut")
print(unsorted_array)

# if you clear your array
unsorted_array.clear()
print(unsorted_array)
unsorted_array.append("Gua Mara KHA")
print(unsorted_array)


unsorted_array = [34, 7, 23, 64, 12, 98, 45, 2, 29, 56]
print(unsorted_array)
print("When we subtrsct 2 in 100,we get",unsorted_array[5])

# if i print any number of the arrys, only inter his index number
print(unsorted_array[8])
print(unsorted_array[4])
print(unsorted_array[6])

# if you calculate the length of your arrays
print("Length of arrays",len(unsorted_array))

# sort your array
unsorted_array.sort()
print(unsorted_array)
# The sorted array is [2, 7, 12, 23, 29, 34, 45, 56, 64, 98]

# remove "12" in your array with pop method
unsorted_array.pop(2)
print(unsorted_array)

# remove "34" in the array with remove method
unsorted_array.remove(34)
print(unsorted_array)

# add somthing
unsorted_array.append(100)
print(unsorted_array)

# if you want sort your arry string wies
for x in unsorted_array:
    print(x)
    
# if you clear your arrays
unsorted_array.clear()
print(unsorted_array)
unsorted_array.append("THANK YOU SO MUCH Bndhu")
print(unsorted_array)