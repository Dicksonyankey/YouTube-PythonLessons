# 4. Write a program that prints the numbers from 1 to 10, but for multiples of three prints "Fizz" instead of the number, and for the multiples of five prints "Buzz". For numbers which are multiples of both three and five, the program should print "FizzBuzz".


# Set the initial value of the loop variable
i = 1

# Start the while loop
while i <= 10:
    # If the loop variable is a multiple of both three and five, print "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # If the loop variable is a multiple of three, print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    # If the loop variable is a multiple of five, print "Buzz"
    elif i % 5 == 0:
        print("Buzz")
    # If the loop variable is not a multiple of three or five, print the number
    else:
        print(i)

    # Increment the loop variable
    i += 1
