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



if __name__ == "__main__":
    # calling the welcome_user and passing in the transform_to_upper function as an arugument.
    welcome_user(transform_to_upper)

    add = add_integer(20)
    print(add())  # 30

    # Calling the function and Storing it in a variable.
    upper = transform_to_upper
    # calling the variable upper and paasing in the arugument.
    print(upper("python programming"))

    

    
