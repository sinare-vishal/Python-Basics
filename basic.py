print("india", "pakistan ", "yeola" , sep = "-")
print("india",end="\n") 
print("hello")

#pyton support 3  categories of the data type :
# 1> basic type : integer , float , complex, boolean, string 
# 2> container type : list , tupple , sets and dictionary
# 3> user defined : class 

# integer range :- 1e309(infinity )
# float range :- 1.7e308



# list = array in python 
# tuple = same as array but use ( )
# sets = use {},  same as arry 




# variable :-(no need to decleare variable before use in the py )
#  dyanamic typing :- no need to declare the type of the data 
name = "vishal"
print(name)
name = 23
print(name)
# we can change the value of the variable ...but in c and cpp we can't ....and this is called dynamic biniding .

# satic typing :- where type of the data is mentioned  


a=4;b=4
print(a,b, sep=",")

# KEywords :-
# py is a case sensative prog. lang (A and a diffrent )
# we cant use the word as a variable which py already declered like if ,import , while etc ...
 
# identifier :-
# rule to define the variable 
# can only start with the alphabet or  _
#followed by 0 or more letter , _ and digit 
_=7
print(_)

# Input from the user :
#value = input("Enter your name:- ")
#print("the value is:-",value)

# whatever we write in the input it going as a string format beacuse string is a universal format (everthing is a can write in the string )...

# hence we need a Type conversion ....
 

# find type of data ,  use :-
datatype = type(4)
print(datatype)

# Type conversion:-
# type :-Implicit and explicit 
#type conversion is a not a permanant operation like type casting 
a=4.5
print(int(a))
print(a)# both give a seperate output.

# implicit:-
  # conversion which py can do implicitly. ex - 
print(4+4.4) 
print(1+2+3j)
print(3+4.5+5j)

# explicit:- 
  # conversion whew we need to mention ourself , ex -
value = int('45') 
print(value)
value = float(4)
print(value)
value = str(4)
print(type(value))
#same for the list ,tuple ,complex ,dectionary etc ...


