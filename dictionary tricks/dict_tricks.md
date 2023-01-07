## First Class Functions in Python

Python has a feature that is unqiue among other programming languages that's treating it's functions as first-class objects. They may be stored in data structures, passed as aruguments, or used to control structures, now this makes Python functions a one of a kind and aslo fun to work with. 


A programming language is said to support first-class functions if it treats functions as first-class objects.


**properties of a first-class functions**
1. A function is an instance of an object type.
2. you can store function in a variable.
3. you can pass the function as an parameter to another function.
4. you can return the function



**Example to demostrate first-class functions in Python**

1. Storing a function in a variable.
The importances of this is that Python functions are able to retain state between calls. This is because functions are objects that can be assigned to variables, and these variables can hold onto their state between function calls.

```python
def transform_to_upper(text:str) -> str:
    return text.upper()


# Calling the function and Storing it in a variable.
upper = transform_to_upper

# calling the variable upper and paasing in the arugument.
print(upper("python programming"))

```

2. passing the function as an parameter to another function.

now because functions are objects in python, they can be a parameter to other functions.

```python
# Let's write a program that welcome a user by shouting the welcome message.

# The function will accept a function as a parameter.

def welcome_user(func):
    welcome = func("hi there, welcome to learning about first-class functions in python")
    print(welcome)

# calling the welcome_user and passing in the transform_to_upper function as an arugument.

welcome_user(transform_to_upper)

```

3. A functions that returns another function

```python
def add_integer(x):
    def add_ten():
        return x + 10

    return add_ten

add = add_integer(20)
print(add()) # 30

```

First-class functions are a powerful feature of Python, and can be used in a variety of ways to make your code more flexible and reusable. Whether you are passing functions as arguments, returning them from other functions, or assigning them to variables, first-class functions can help you write code that is more elegant and efficient.