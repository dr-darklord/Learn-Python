'''There are two types are "Type casting"
1.Explicit conversation (its based on me)
2.Implicit conversation (its based on python)
Here "a" and "b" is a string data type who convert in an "integer".'''
'''
# Explicit conversation Type casting 
a = "100" #string type 
b = "100"
print(int(a) + int(b))

a = "15"
b = 7 #integer type
sum =(int(a) + b)
print("The addition is : ",sum) '''

# Implicit conversation Type casting
a1= 9.5
b2 = 91
sum = (a1+b2)
print("Here \"a1\" is a : ",type(a1),"Number")
print("Here \"b2\" is a : ",type(b2),"Number")
print("The addition of Both Number : ",sum)
print("it is" , type(sum),"Number")