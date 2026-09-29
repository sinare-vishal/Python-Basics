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

#LITERALS :-
# literal is a raw data given in a variable. in py heres the type :-
# 1. Numeric literal
# 2. string literal
# 3. boolean literal 
# 4. special literal 

#Numerial:-it include diffrent type such as 
a= 0b10101 #Binary literal , output - 10
b= 100 # decimal literal , output - 100
c= 0o310 #octal literal ,output - 200
d = 0x12c #hexadecimal literal , output - 300

#float literal:
float_1= 10.5  #o/p - 10.5
float_2 = 1.5e2  #o/p - 150.0
flaot_3 = 1.5e-3  #o/p - 0.0015

#complex literal :-
# in which we can extract the imaginery and the real part of the literal like ..
x = 3.14j
print(x,x.imag,x.real)

# String literals :-
#for multiple line used """..... """ 
#for unicode (sticker/emoji) used u :-
unicode = u"\U0001F600"
print(unicode)
#for raw string (if it include special symbol like /n etc) used:-
raw_str = r" raw \n string"
print(raw_str)

#Boolean literal:-
a=True + 3 #it consider true  as 1 so o/p = 4

#special literals :- in these we assign value as a none to the variable to just keep the variable in the program ...
k=None

####Operators:-

