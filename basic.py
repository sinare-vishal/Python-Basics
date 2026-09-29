
# ==========================================================
#                    PYTHON BASICS NOTES
# ==========================================================

#=======================================================
# 1. print()
#=======================================================
print("india", "pakistan", "yeola", sep="-")
# Output: india-pakistan-yeola

print("india", end="\n")
print("hello")

# sep -> separates multiple values
# end -> specifies what to print at the end
# Default end = "\n"

# =======================================================
# 2. DATA TYPES
# =======================================================

# Basic / Built-in types:
# int       -> Integer
# float     -> Decimal number
# complex   -> Complex number
# bool      -> True / False
# str       -> String

# Collection types:
# list      -> Ordered, mutable collection
# tuple     -> Ordered, immutable collection
# set       -> Unordered collection of unique values
# dict      -> Key-value pairs

# User-defined:
# class     -> Used to create user-defined types


# ============================================================
# 3. INTEGER AND FLOAT
# ============================================================

# Python integers have arbitrary precision.
# They are NOT limited to a fixed range like C/C++ integers.

a = 123456789012345678901234567890
print(a)

# Python float usually uses 64-bit floating-point representation.
# Approximate maximum float:
# 1.8 × 10^308


# ============================================================
# 4. VARIABLES
# ============================================================

# No need to declare a variable before using it.

name = "vishal"
print(name)

name = 23
print(name)

# Python is dynamically typed.
# The same variable name can refer to objects of different types.

x = 10
x = "hello"


# ============================================================
# 5. DYNAMIC TYPING
# ============================================================

# Dynamic typing:
# We don't have to explicitly declare the data type of a variable.

x = 10          # int
x = 10.5        # float
x = "Vishal"    # str


# ============================================================
# 6. DYNAMIC BINDING
# ============================================================

# Dynamic binding means a name can be bound to different
# objects during program execution.
x = 10
x = "hello"
# ============================================================
# 7. STATIC TYPING
# ============================================================

# In statically typed languages, the type is declared/known
# as part of the program.

# Example in C/C++:
# int x = 10;


# ============================================================
# 8. MULTIPLE ASSIGNMENT
# ============================================================

a = 4
b = 4

print(a, b, sep=",")

# Python also supports multiple assignment:

a, b = 10, 20
print(a, b)


# ============================================================
# 9. KEYWORDS
# ============================================================

# Python is case-sensitive.

name = "Vishal"
Name = "ABC"

# name and Name are different variables.

# Keywords are reserved words in Python.
# They cannot normally be used as variable names.

# Examples:
# if, else, for, while, import, class, def, return,
# True, False, None

import keyword

print(keyword.kwlist)


# ============================================================
# 10. IDENTIFIERS
# ============================================================

# Identifier = name given to a variable, function, class, etc.

# Rules:
# 1. Can contain letters, digits and underscore (_)
# 2. Cannot start with a digit
# 3. Can start with a letter or underscore
# 4. Cannot be a Python keyword
# 5. Python is case-sensitive

student_name = "Vishal"
_age = 21
student1 = "ABC"

# Invalid examples:
# 1name = "Vishal"
# class = 10

# =======================================================
# 11. INPUT FROM USER
# =========================================================
#value = input("Enter your name: ")
#print("The value is:", value)

# input() always returns a STRING.

#age = input("Enter age: ")
#print(type(age))

# Output:
# <class 'str'>

# Therefore, type conversion is required when necessary.
age = int(input("Enter your age: "))
print(age)

# =======================================================
# 12. TYPE OF DATA
# =========================================================

datatype = type(4)
print(datatype)

# Output:
# <class 'int'>

# =========================================================
# 13. TYPE CONVERSION
# =========================================================
# Type conversion means converting one data type into another.

# Two types:
# 1. Implicit conversion
# 2. Explicit conversion


# ------------------------------------------------------------
# 13.1 IMPLICIT TYPE CONVERSION
# ------------------------------------------------------------

# Python automatically converts the type when appropriate.

print(4 + 4.4)
# Output: 8.4

# int + float -> float


# ------------------------------------------------------------
# 13.2 EXPLICIT TYPE CONVERSION
# ------------------------------------------------------------

# Programmer explicitly performs the conversion.

value = int("45")
print(value)

value = float(4)
print(value)

value = str(4)
print(type(value))


# Common conversion functions:
# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()
# complex()


# Type conversion does not change the original variable
# unless we assign the converted value back.

a = 4.5

print(int(a))   # 4
print(a)        # 4.5

# To permanently store the converted value:
# a = int(a)


# ============================================================
# 14. LITERALS
# ============================================================

# Literal = a value written directly in the source code.

age = 21
name = "Vishal"

# 21 and "Vishal" are literals.

# Common types of literals:
# 1. Numeric literals
# 2. String literals
# 3. Boolean literals
# 4. Special literal (None)


# ============================================================
# 15. NUMERIC LITERALS
# ============================================================

# Binary literal
# Prefix: 0b

a = 0b1010
print(a)
# Output: 10


# Decimal literal

b = 100
print(b)
# Output: 100


# Octal literal
# Prefix: 0o

c = 0o310
print(c)
# Output: 200


# Hexadecimal literal
# Prefix: 0x

d = 0x12C
print(d)
# Output: 300
# ==========================================================
# 16. FLOAT LITERALS
# =========================================================

float_1 = 10.5
print(float_1)
# Output: 10.5

float_2 = 1.5e2
print(float_2)
# Output: 150.0

float_3 = 1.5e-3
print(float_3)
# Output: 0.0015

# e represents scientific notation.


# ============================================================
# 17. COMPLEX LITERALS
# ============================================================

# Python uses 'j' for the imaginary part.

x = 3.14j

print(x)
print(x.real)
print(x.imag)

# Example:
x = 3 + 4j

print(x.real)   # 3.0
print(x.imag)   # 4.0


# ============================================================
# 18. STRING LITERALS
# ============================================================

name = "Vishal"
name = 'Vishal'

# Both are valid strings.
# -----------------------------------------------------------
# Multiline String
# ---------------------------------------------------------
message = """Hello
Welcome to Python
Learning Python"""
print(message)
# ----------------------------------------------------------
# Unicode
# ----------------------------------------------------------
# Python 3 strings support Unicode by default.

emoji = u"\U0001F600"
print(emoji)

# The old 'u' prefix is not normally required in Python 3.
# ----------------------------------------------------------
# Raw String
# ----------------------------------------------------------
# Raw strings treat backslashes mostly as literal characters.

raw_str = r"raw \n string"
print(raw_str)

# Output:
# raw \n string

# ========================================================
# 19. BOOLEAN LITERALS
# ==========================================================
# Python has two Boolean values:

# True
# False

a = True

print(a)

# True behaves like 1 in numeric operations.
# False behaves like 0.

a = True + 3
print(a)
# Output: 4

# =========================================================
# 20. SPECIAL LITERAL - None
# ==========================================================
# None represents the absence of a value.
k = None
print(k)

# Commonly used when a variable currently has no value.
# ==========================================================
# 21. COLLECTION TYPES
# ==========================================================
# ---------------------------------------------------------
# LIST
# ----------------------------------------------------------

# Ordered
# Mutable
# Allows duplicate values

numbers = [10, 20, 30, 20]
print(numbers)
# ---------------------------------------------------------
# TUPLE
# ----------------------------------------------------------
# Ordered
# Immutable
# Allows duplicate values

numbers = (10, 20, 30, 20)
print(numbers)
# ---------------------------------------------------------
# SET
# ---------------------------------------------------------
# Unordered
# Stores unique values
# Mutable

numbers = {10, 20, 30, 20}

print(numbers)
# Duplicate 20 is removed.
# ---------------------------------------------------------
# DICTIONARY
# ---------------------------------------------------------
# Stores data in key-value pairs.

student = {
    "name": "Vishal",
    "age": 21
}
print(student)

# IMPORTANT:
# List is NOT exactly the same as an array.
# Python list is a dynamic, general-purpose collection
# that can store objects of different types.
# ============================================================
# 22. OPERATORS
# ============================================================

# Arithmetic:
# +   -   *   /   //   %   **

# Comparison:
# ==   !=   >   <   >=   <=

# Logical:
# and   or   not

# Assignment:
# =   +=   -=   *=   /=

# Bitwise:
# &   |   ^   ~   <<   >>

# Membership:
# in   not in

# Identity:
# is   is not
# Example:
a = 10
b = 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000

