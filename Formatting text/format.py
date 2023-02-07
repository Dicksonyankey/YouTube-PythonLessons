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