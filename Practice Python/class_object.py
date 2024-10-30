'''Create a Class
To create a class, use the keyword "class:"

Example
Create a class named MyClass, with a property named x:'''
class MyClass:
  x = 5

print(MyClass)


'''Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:
'''
class MyClass:
  x = 5
  
p1 = MyClass()
print(p1.x)


'''The __init__() Function
The examples above are classes and objects in their simplest form, 
and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), 
which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:'''
details=[]
class Person:
    def __init__(self):
        self.name = input("Enter Your Name : ")
        self.age = input("Enter Your Age : ")
        # print(self.name,self.age)
        details.append(self.name + " " + self.age) 
        
               
p1 = Person()
p2 = Person()  
for x in details:
    print(x)
# print(f"welcome {name} Sir,Your age {age}.")
# print(p1.name)   
# print(p1.age)   
# print(p2.name)  
# print(p2.age)

# print(p1.name,p1.age, p2.name,p2.age)   