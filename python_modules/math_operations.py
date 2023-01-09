
def addition(a: int, b: int) -> int:
    """Returns the sum of of two numbers"""
    return a + b


def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers"""
    return a * b


def division(dividend: int, divisor: int) -> float:
    """
    Performs the division operation between the dividend
    and divisor
    """
    return dividend / divisor


def factorial(n):
    """Returns the factorial of n"""
    i = 0
    result = 1
    while (i != n):
        i = i+1
        result = result * i
    return result
