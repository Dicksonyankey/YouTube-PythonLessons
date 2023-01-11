# let's finally take a look at a Counter Example with the while loop.

import random
limit = 5
count = 0
while count != limit:
    print(f"Shouting {count}")
    count += 1


# Another example of the counter

user_data = 3
count = 0
while count != user_data:
    for x in range(1, 3):
        print("fighting !!!!")
    else:
        print(f"Done fighting! {count + 1} time")

    count += 1


# The break keyword

user_data = 10
count = 0
while count != user_data:
    print(f"Displaying the Number {count}")
    if count == 6:
        print("Hey, am been asked to break out of the loop")
        break
    count += 1
print("Am out of the loop now")


# The continue keyword

count = 1
while count <= 10:
    if count == 6:
        count += 1
        continue
    print(f"Display the number {count}")
    count += 1
print('Not in WHILE loop.')


# More Examples

while True:
    line = input('Tell me something: ')
    if not line == '':
        print(line)
        continue
    else:
        break
print('End of the program')


# 1. Write a program that counts down from 10 to 1 and then prints "Liftoff!"

# Set the initial value of the loop variable
i = 10
# Start the while loop
while i > 0:
    # Print the value of the loop variable
    print(i)
    # Decrement the loop variable
    i -= 1
# Print "Liftoff!" after the loop finishes
print("Liftoff!")


# 2. Write a program that asks the user to enter a number, and keeps asking until the user enters a number greater than 100.

# Start an infinite loop
while True:
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    # If the number is greater than 100, break out of the loop
    if num > 100:
        break
# Print a message after the loop finishes
print("Thank you for entering a number greater than 100.")


# 3. Write a program that generates a random number between 1 and 10 and asks the user to guess it. The program should continue asking the user to guess until they get it right.


# Generate a random number between 1 and 10
secret_num = random.randint(1, 10)
# Start an infinite loop
while True:
    # Ask the user to guess the number
    guess = int(input("Enter a guess: "))
    # If the guess is correct, break out of the loop
    if guess == secret_num:
        break
# Print a message after the loop finishes
print("Congratulations, you guessed the correct number!")


# ------------------Exercise to play with-------------
# 4. Write a program that prints the numbers from 1 to 10, but for multiples of three prints "Fizz" instead of the number, and for the multiples of five prints "Buzz". For numbers which are multiples of both three and five, the program should print "FizzBuzz".
