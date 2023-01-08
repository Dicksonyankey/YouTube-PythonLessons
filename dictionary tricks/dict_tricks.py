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

    return f"This operator '{operator}' doesn't exist."



# Secod code example. treating the function as a first class function.
# it is returning a dictionary object and the same time calling itself.
def dispatch_dictionary(operator: str, x: int, y: int) -> float:
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mult": lambda: x * y,
        "div": lambda: x / y
    }.get(operator, lambda: None)()


def string_methods(method_name: str, text: str) -> str:
    if method_name == "lower":
        return text.lower()
    elif method_name == "upper":
        return text.upper()
    elif method_name == "casefold":
        return text.casefold()
    elif method_name == "strip":
        return text.strip()

    return f"This methods '{method_name}' doesn't exist."


def dict_solution(method_name: str, text: str) -> str:
    return {
        "lower": lambda: text.lower(),
        "upper": lambda: text.upper(),
        "casefold": lambda: text.casefold(),
        "strip": lambda : text.strip()
    }.get(method_name, lambda: f"This methods '{method_name}' doesn't exist.")()


if __name__ == "__main__":
    print(dispatch_arithmetic("add", 10, 10))
    print(dispatch_arithmetic("sub", 10, 10))
    print(dispatch_arithmetic("mult", 10, 10))
    print(dispatch_arithmetic("multi", 10, 10))
    print(dispatch_arithmetic("div", 10, 10))


    print(dispatch_dictionary("add", 10, 10))
    print(dispatch_dictionary("sub", 10, 10))
    print(dispatch_dictionary("mult", 10, 10))
    print(dispatch_dictionary("div", 10, 10))
    print(dispatch_dictionary("floor div", 10, 10))

    print(dict_solution("lower", "PYTHON PROGRAMMING"))
    print(dict_solution("upper", "python programming"))
    print(dict_solution("strip", "python programming"))
