# --------------------- str.format() mwthod ----------------------
# Declaring a pie variables 

pie = 3

print("I ate some {} and it was yummy".format(pie))

name = "Jane Smith"
age = 30
salary = 12000

# We casting the number values to string since we are working with only string.
print("Hello there, My name is {}. i'm {} years old and my salary is ${}".format(name, str(age), str(salary)))



# ------------------ Formatted String ----------------------
name = "Jane Smith"
age = 30
salary = 12000

print(f"Hello there, My name is {name}. i'm {age} years old and my salary is ${salary}")


# -------------------------- String Concatenation ------------------

# Declaring two variables 
number1 = 100
number2 = 200

# Adding the two variables and storing the value to a variables called result.
result = number1 + number2
print(result)
```
Here is another example
```python 
# Declaring some varibales 

name = "Jane Smith"
age = 30
salary = 12000

print("Hello there, " + "My name is " + name + " . I am " + str(age) + " years old and my salary is $" + str(salary) + ".")


# -------------------------- Formatting float as integer ------------------

# Declaring a floating point number 
number = 9.98747

# Formatting the floating point number into an integer
print(f"{number:.0f}") # 10

# Example 2 

number1 = 29.3674

print("{:.0f}".format(number1))



# -------------------------- Rounding floaing numbers from 1 - n decimal places ------------------

# Declaring a floating point number 
number = 9.98747

# Formatting the floating point number into an integer
print(f"{number:.1f}") 


number1 = 29.3674
# Rounding to 2 decimal places 
print("{:.2f}".format(number1))


number2 = 10.36746736
# Rounding to 4 decimal places 
print("{:.4f}".format(number1))


number3 = 29.367478928874
# Rounding to 6 decimal places 
print("{:.6f}".format(number1))


# -------------------------- Formatting a floating number as percentage ------------------

# finding 25 percent of 150
number = 150
result = (25/100) * number
print(f"The finally answer is {result:.2f}") # 37.50


# finding the percentage of 37.50 in 150
num1 = 37.50
num2 = 150
result1 = (num1/num2) * 100
print(f"The finally answer is {result1:.2f}%") # 25.00%


# -------------------------- Left padding ------------------

print("{:>4}".format(5.9980))

print("{:>7}".format(5.9980))

# The list of items
tables = ["Books", "Mobile phones", "Laptops", "Magic Keyboard"]

# This is a format for the heading
print("{}{:>15}".format("Number","Items"))

# This for loop will populate the data into the headers.
for indx, item in enumerate(tables):
    print("{:>3}{:>20}".format(indx, item))


# -------------------------- Right padding ------------------

# make a full size of 7 and fill with zero to the right
print("{:<07}".format(5.9980))

# make a full size of 20 and fill with zero to the right
print("{:<020}".format(5.9980))


# TO also center a text you can use;
print('{:^24s}'.format("MyString"))

# To separate integers with commas eg. 5,000,000
print('{:,}'.format(5000000))


# To format by add .00 to the last value eg. 1,000.00
print('{:,.2f}'.format(1000))