# Variables In Python 

**What you will learn**
1. What is variable in python
2. How to declare a variable in python
3. Rules for Naming a variable in python
4. Assigning a single value to multiple Variables
5. Global vrs Local Keyword in python
6. Rules for the global Keyword
7. Constants in python




### What is variable in python.
Python Variable is  a container which store values. Python is not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it.We can also say that Python variables are the reserved memory locations used to store values with in a Python Program. This means that when you create a variable you reserve some space in the memory.


### How to declare a variable in python.
A Python variable is created automatically when you assign a value to it. The equal sign `(=)` is used to assign values to variables.
Here let's declare a variable in python;

```python
# declaring a variable in python

my_name = "Python Programming"
print(my_name)


# declaring another varibale in Python

number = 100
print(number)

# declaring another variable

salary = 120000.1234
print(salary)

# declaring another variable

drug_name = "Paracetamol"
print(drug_name)
```


### Rules for Naming a variable in python.
1. Variable names should be very descriptive.
2. A variable name must start with a letter or the underscore character.
3. A variable name cannot start with a number or any special character like `$, (, * %` etc.
4. A variable name can only contain alpha-numeric characters and underscores `(A-z, 0-9, and _ )`.
5. Variable names are case-sensitive (age, Age and AGE are three separate variables).
6. The reserved words(keywords) cannot be used naming the variable.


### Assigning a single value to multiple Variables.
Also, Python allows assigning a single value to several variables simultaneously with `=` operators. 

```python
# Assigning a single value to multiple variables

x = y = z = 100.00
print(x) # 100.0
print(y) # 100.0
print(z) # 100.0


# Another example 

a = b = c = 15
print(a) # 15
print(b) # 15
print(c) # 15

```


### Global vrs Local Keyword in python

**Local Variable**
Local variables are the ones that are defined and declared inside a function. We can not call this variable outside the function.

```python 
# Local Variables

def add_number():
    x = 10
    y = 20
    result = x + y
    return f"The total number = {result}"

print(add_number())

```
**Global Variable**
A variable declared outside the function is the global variable by default. Python provides the global keyword to use global variable inside the function. If we don't use the global keyword, the function treats it as a local variable. Let's understand the following example.

```python 
# Initializing a Global variable
message = "I LOVE PYTHON PROGRAMMING"

def display_msg():
    global message

    # local variable
    msg = "Coding is Fun."
    
    # The (\n) stands for new line.
    return f"Global : The message is  '{message}', \nLocal : The message is '{msg}'"

print(display_msg())

```

### Rules for the global Keyword.
1. If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
2. We Use global keyword to use a global variable inside a function.
3. There is no need to use global keyword outside a function.


### Constants in python.
A constant is a special type of variable whose value cannot be changed.

```python
# Constants in python

PI = 3.142
GRAVITY = 9.8

print(PI)
print(GRAVITY)


```


