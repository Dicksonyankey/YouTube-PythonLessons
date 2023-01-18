## <u>WHILE LOOP AND HOW THEY WORK IN PYTHON</u>

**What you will learn**

### 1. <u>what are loops in python </u>

Loops are a fundamental programming concept that allow a program to execute a block of code multiple times.They allow a program to perform repetitive tasks efficiently. However we can also say that loops are sequence of instructions that is continually repeated until a condition is reached.

### 2. <u>The while statement</u>
- Syntax of while loops
- counter example 

The while statement in python is used to repeat execution of code or block of code that is controlled by a conditional expression. let's look at the  syntax for a while loop in the code below:

```python
while conditional expression:
     code statement 0
     code statement 1
     code statement 2
     ...
     code statement n

```
let's finally take a look at a Counter Example with the while loop.

```python
limit = 5
count = 0
while count != limit:
    print(f"Shouting {count}")
    count += 1

```
so this is using the while loop to implement a counter in python. below is another example

```python
user_data = 3
count = 0

while count != user_data:
    for x in range(1,3):
        print("fighting !!!!")
    else:
        print(f"Done fighting! {count + 1} time")
        
    count += 1
    
```


### 3. <u>using both while and for loop</u>
we can also use while with for some common task in python. let's take a look at some example.

```python
user_data = 3
count = 0
while count != user_data:
    for x in range(1, 3):
        print("fighting !!!!")
    else:
        print(f"Done fighting! {count + 1} time")

    count += 1


```
### 4. <u>Loop control statements</u>
    - the break keyword
    - the continue keyword
    - the pass keyword
    - the difference between comments and pass keyword

Python provides various ways to change the code execution flow during the execution of loops and they are break, continue and  pass.

1. The break keyword is used to break the execution flow of a loop. When used inside a loop, this keyword stops executing the loop.

**Example**
```python
user_data = 10
count = 0
while count != user_data:
    print(f"Displaying the Number {count}")
    if count == 6:
        print("Hey, am been asked to break out of the loop")
        break
    count += 1
print("Am out of the loop now")

```

2. The continue keyword  will skip the current iteration and continue with the next iteration. let's take an example.
```python
count = 1
while count <= 10:
    if count == 6:
        count += 1
        continue
    print(f"Display the number {count}")
    count += 1
print('Not in WHILE loop.')
```

3. The pass keyword is not used to alter the execution flow, but rather it is used merely as a placeholder.  



4. The only difference between a comment and a pass statement in Python is that the interpreter will entirely ignore the comment whereas a pass statement is not ignored. However, nothing happens when pass is executed.

### 5. <u>Example to play with</u>

```python
while True:
    line = input('Tell me something: ')
    if not line == '':   
        print(line)
        continue    
    else:  
        break 
print('End of the program')
```

1. Write a program that counts down from 10 to 1 and then prints "Liftoff!"
```python 
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

``` 

2. Write a program that asks the user to enter a number, and keeps asking until the user enters a number greater than 100.
```python
# Start an infinite loop
while True:
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # If the number is greater than 100, break out of the loop
    if num > 100:
        break

# Print a message after the loop finishes
print("Thank you for entering a number greater than 100.")
```

3. Write a program that generates a random number between 1 and 10 and asks the user to guess it. The program should continue asking the user to guess until they get it right.

```python
import random
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

```

4. Write a program that prints the numbers from 1 to 10, but for multiples of three prints "Fizz" instead of the number, and for the multiples of five prints "Buzz". For numbers which are multiples of both three and five, the program should print "FizzBuzz".


```python
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

```
### 6. <u>Main takeaway.</u>
1. Loops are used to perform iterative process. In other words, loops are used to execute the same code more than one.
2. A counter needs to be coded  explicitly for while loop.
3. The break keyword is used to break the executionof a loop.
4. The continue keyword is used to skip the current iteration and moves to the next iteration.
5. The pass keyword is used as a placeholder in an empty loop. 