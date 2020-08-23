"""@Author: Maria DaRocha
    Date: 23-8-2020

    Title: Python Tutoring Session One
    @Topics: Python 3 Basics
        Arithmatic Operators
        Boolean Operators
        Importing
        Lists
        Print
        Strings
        Type Checking

    @Source: https://www.learnpython.org
"""

#Demo a simple function
def run_basic_tasks(): 
    #Strings
    my_name = "Maria"
    print("Hello and welcome " + my_name + "!")

    #Variables
    x = 1
    if x == 1:
        # indented four spaces
        print("x is 1.")

    #Float assignment
    myfloat = 7.0
    print(myfloat)

    myfloat = float(7)
    print(myfloat)

    #String assignment
    mystring = 'hello'
    print(mystring)

    mystring = "hello"
    print(mystring)


# Demo some numeric operators
def operator_fun():
    # a = 1
    # b = 2
    a, b = 1, 2
    # Addition
    c = a + b
    print(str(a) + " + " + str(b) + " = " + str(c))
    # Subtraction
    c = a - b
    print(str(a) + " - " + str(b) + " = " + str(c))
    # Multiplication
    c = a * b
    print(str(a) + " * " + str(b) + " = " + str(c))
    # Division
    c = a / b
    print(str(a) + " / " + str(b) + " = " + str(c))
    # Modulo (Remainder)
    c = a % b
    print(str(a) + " % " + str(b) + " = " + str(c))
    # Concatinate strings
    hello = "hello"
    world = "world"
    helloworld = hello + " " + world
    print(helloworld)
    # Square a number
    square = 7 ** 2
    print("Seven to the power of two = %d" % square)
    # Cube a number
    cube = 7 ** 3
    print("Seven to the power of three = %d" % cube)

# Demo type-checking
def type_checking():
    mystring = 'hello'
    myfloat = float(10)
    myint = 20

    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)


# Demo print function syntax
def print_fun():
    # This prints out whatever values a and b are with a '+' in between
    a, b = 11, 234
    print("%d + %d" % (a,b))

    # This prints out "John is 23 years old."
    name = "John"
    age = 23
    print("%s is %d years old." % (name, age))

    # This prints out: A list: [1, 2, 3]
    mylist = [1,2,3]
    print("A list: %s" % mylist)

    # Get the length of a string
    astring = "hello"
    print("hello is %d letters long" % len(astring))

    # printing strings astring[start:stop:step]
    astring = "Hello world!"
    print(astring[3:7])
    print(astring[3:7:1])
    
    #String manipulation
    # prints "!dlrow olleH"
    print(astring[::-1])
    # Uppercase
    print(astring.upper())
    # Lowercase
    print(astring.lower())
    # Startswith and Endswith
    print(astring.startswith("Hello")) # TRUE
    print(astring.endswith("asdfasdfasdf")) # FALSE
    # Split string by a character (becomes a list)
    two_words = astring.split(" ")
    print("Two words: %s" % two_words)



# Demo lists
def list_fun():
    mylist = []
    mylist.append(4)
    mylist.append("Aaron")
    mylist.append(17)
    #print(mylist[0]) # prints first number appended
    #print(mylist[1]) # prints second number appended
    #print(mylist[2]) # etc

    # prints out values of list on separate lines
    for x in mylist:
        if isinstance(x, int):
            print(x)

    # prints out My List: [x, y, z, etc..]
    print("My list: %s" % mylist)


# Demo boolean operators
def boolean_fun():
    x = 2
    # Equal to
    print(x == 2) # prints out True
    print(x == 3) # prints out False
    # Less than
    print(x < 3) # prints out True
    # Greater than
    print(x > 3) # prints out False
    # NOT equal to
    print(x != 3) # prints out True
    
    # And operator
    if x == 2 and x < 3: # True
        print(x == 2 and x > 3) # False

    # In operator
    name = "John"
    if name in ["John", "Rick"]:
        print("Your name is either John or Rick.")

    # Is operator
    x = [1,2,3]
    y = [1,2,3]
    print(x == y) # Prints out True
    print(x is y) # Prints out False

    # Not operator
    isthislit = (x is y) # False -> This is not lit
    print(not isthislit) # Prints out True -> Now it's lit again
    print((not True) == (False)) # Prints out True -> Not true is false

# IN THE NEXT SECTION...
# Loops
# Demo save function
# Demo load function