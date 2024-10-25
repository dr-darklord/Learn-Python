#"TEXT/string type Data type"
group_name = "The Unbreakable Neural Network"#must use double cottation
print(group_name)
myname="Sakib."
print("My name is " + ' ' + myname )
print(type(group_name))#identify type

#"NUMERIC/NUMBER Data type"
sakib_phone_number=1701639086
print(sakib_phone_number)
print(type(sakib_phone_number))

#Float data type
MD_Mahamudul_cgpa=3.95
print(MD_Mahamudul_cgpa)
print(type(MD_Mahamudul_cgpa))

#Complex data type
Ahasun=420j #FOR Complex data TYPE YOU Have must used "j"
print(Ahasun)
print(type(Ahasun))

#Boolean data type
sakib=6.6
mahamudul=6.5
print("MD.Mahamudul is taller than sakib")
print(sakib<mahamudul)
a=8
b=7
print("Boys don't masturbate.")
print(a<b)
print(type(a<b))
a=10
b=9
print("Boys do masturbate.")
print(a>b)
print(type(a>b))

#String Formating
num1=100
num2=100
print(f"Addition of two number {num1+num2}.")

#Binary data type
#here discuss bytes
bin=[1,2,4,65,4,3,44,33]
r = bytes(bin)
print(r)
print(type(r))

#Bitearry discussion
ms=[1,3,5,7,2,6,88,99]
r1=bytearray(ms)
r1[5]=222
print(r1[5])
print(type(r1))

#None type data
q=None
print(q)
print(type(q))

#Sequence type data = list
li=["mango","banana","kathal","coconat"]
li[2]='Jackfruit'
print(li)
print(type(li))

#Sequence type data = Tuple
tu=(1,2,3,4,5,6,7,8)
print(tu)
print(type(tu))

#Sequence type data = Range
ra=range(8)
print(ra)
for i in ra:
    print(i)
    print(type(ra))