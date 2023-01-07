def transform_to_upper(text: str) -> str:
    return text.upper()


def welcome_user(func):
    welcome = func(
        "hi there, welcome to learning about first-class functions in python")
    print(welcome)


def add_integer(x):
    def add_ten():
        return x + 10
    return add_ten

# -------  Dictionary trick that you can implement -----------

# First code exaple is the same as the second code
def dispatch_arithmetic(operator: str, x: int, y: int) -> float:
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mult":
        return x * y
    elif operator == "div":
        return x / y


# Secod code example. treating the function as a first class function.
# it is returning a dictionary object and the same time calling itself.
def dispatch_dictionary(operator: str, x: int, y: int) -> float:
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mult": lambda: x * y,
        "div": lambda: x / y
    }.get(operator, lambda: None)()




if __name__ == "__main__":
    print(dispatch_arithmetic("add", 10, 10))
    print(dispatch_arithmetic("sub", 10, 10))
    print(dispatch_arithmetic("mult", 10, 10))
    print(dispatch_arithmetic("div", 10, 10))


    print(dispatch_dictionary("add", 10, 10))
    print(dispatch_dictionary("sub", 10, 10))
    print(dispatch_dictionary("mult", 10, 10))
    print(dispatch_dictionary("div", 10, 10))
    print(dispatch_dictionary("floor div", 10, 10))

    # calling the welcome_user and passing in the transform_to_upper function as an arugument.
    welcome_user(transform_to_upper)

    add = add_integer(20)
    print(add())  # 30

    # Calling the function and Storing it in a variable.
    upper = transform_to_upper
    # calling the variable upper and paasing in the arugument.
    print(upper("python programming"))


    
