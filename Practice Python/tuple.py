# One item tuple, remember the comma:
thistuple = ("apple","pepe",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

'''Tuple items can be of any data type:
Example
String, int and boolean data types: '''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

''' if you create a tuple use the tuple() constructor to make a tuple.
Example
Using the tuple() method to make a tuple: '''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)