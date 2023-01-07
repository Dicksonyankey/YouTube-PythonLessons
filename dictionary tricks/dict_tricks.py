def dispatch_arithmetic(operator:str, x:int, y:int) -> float:
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mult":
        return x * y
    elif operator == "div":
        return x / y


def dispatch_dictionary(operator: str, x: int, y: int) -> float:
    return {
        "add": lambda : x + y,
        "sub": lambda: x - y,
        "mult": lambda: x * y,
        "div": lambda: x / y
    }.get(operator, lambda : None)()


if __name__ == "__main__":
    # print(dispatch_arithmetic("add", 10, 10))
    # print(dispatch_arithmetic("sub", 10, 10))
    # print(dispatch_arithmetic("mult", 10, 10))
    # print(dispatch_arithmetic("div", 10, 10))
    print(dispatch_dictionary("add", 10, 10))
    print(dispatch_dictionary("sub", 10, 10))
    print(dispatch_dictionary("mult", 10, 10))
    print(dispatch_dictionary("div", 10, 10))
    print(dispatch_dictionary("floor div", 10, 10))


    
