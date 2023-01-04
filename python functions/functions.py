# BUILT-IN FUNCTIONS
# in some of the tutorials posted we have come across some of the built-in functions such
# print() , type(), range(), help(), input() and others etc. it is time for us to take a look at user defined function that's function that we create by ourselves as we write our program.

# Functions itself come in three differnet forms 
# built-in functions , user defined functions and anonymous functions


# USER DEFINED FUNCTIONS 
# A function is a block of code(that performs a specific task) which runs only when it is called.

# Functions are defined using the def keyword, followed by an identifier name along with the parentheses, and by the final colon that ends the line.

# We write our own function be of 
# 1. Reusability -> To be able the reuse one program in other programs when it is needed
# 2. Modular approah -> breaking down larger problems into smaller chuncks and each chunck is implemented via a functions. this makes our function readable and easy to understand

# CREATING A USER DEFINED FUNCTION
# When creatind a user defined function, we need 
# 1. the def keyword,
# 2. followed by an identifier name along with 
# 3. the parentheses, 
# 4. and by the final colon that ends the line.


# Example : creating a user defined function the greets a person

# This is a function that greets a person
def greetPerson() -> None:
    print("Hello there, welcome to python user-defined function!")

# Calling a function : to call function we first write the function name followed by parenthesis.

greetPerson() # And when we run this code we will get an output.

# Example 2: creating a user defined function that will say Hello 

def sayHello() -> None:
    print("Hello User-defined function")

sayHello()


# FUNCTION DOCSTRINGS
# Python has a cool feature called documentation string, usually referred to by its shorter name docstrings.This is an important but not required tool that should be used every time we write a program.

# Docstrings are written within triple single/double quotes just after defini- tion header.They are written on the first logical line of a function.They are not only limited to functions but also classs


# Example : 

def displayName() -> None:
    """
    This function has one local variable called name
    name stores a string value

    Parameter:
    this function has no parameter 

    Returns:
    this functions return nothing
    """
    name = "Jane Smith"
    print(f"My name is {name}")

displayName()


# FUNCTIONS WITH NO PARAMETER

# this is an example of a function with no parameter
def hello():
    print("Helllo there !!")
hello()


# DIFFERNCE BETWEEN PARAMETER AND ARGUMENTS

# parameter are the variables passed inside the parenthesis of the function. A function can have a number of parameters separated by a comma.

# arguments are the values passed inside the parenthesis at the time of a function call. A function can have a number of arguments separated by a comma.


# FUNCTIONS WITH ONLY ONE PARAMETER

def upper_lower(x):
    """
    Returns the upper and lower version of the string.

    The value must be a string, else it will result in
    an error.

    """
    upper = x.upper()  # Convert x to upper string
    lower = x.lower()  # Convert x to lower string
    return upper, lower  # Return both variables

upper_lower("pYtHoN")


# Return statement in Python function
# The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller.


# FUNCTION WOTH MULTIPLE PARAMETERS 

def power(number, pow=2):
    """
    Parameters:
    number : int
    pow : int

    Returns:
    returns the value of number to the power of pow.
    """
    return number ** pow

print(power(3))
print(power(5,2))



# FUNCTION ARGUMENTS AND KEYWORD ARGUEMENTS
def sum_numbers(a,b,c,d,e) -> int:
    return a+b+c+d+e

sum_numbers(1,2,3,4,5)


def sum_numbers1(*a) -> int:
    return sum(a)

sum_numbers1(1,2,3,4,5)



def sum_numbers2(*a) -> int:
    count = 0
    for i in a:
        count += i
    return count
        

sum_numbers2(1,2,3,4,5)


# FOR THE KEYWORD ARGUMENTS 

def person(**kwargs):
    person = {}
    for key, value in kwargs.items():
        person[key] = value
    return person

person(name="Jane smith", job="Developer", age=25, salary=75000, country="United States")