# <u>Formatting Text In Python</u>

String formatting is important when you want to build new strings that are using existing values. Python provides several ways to format text strings. The most popular of these are formatted string, the `str.format()` method, and % formatting.


### **Formatted String**

 Formatted string  is the process of evaluating a string that has placeholders. These placeholders can hold expressions that yield a value, which is then placed inside the string. Special kinds of strings, known as `f-strings` is used during formatted string. These strings are prefixed with an f to denote how they're meant to be interpreted:

**Example**

```python 

name = "Jane Smith"
age = 30
salary = 12000

print(f"Hello there, My name is {name}. i'm {age} years old and my salary is ${salary}")

```


### **The `str.format()` Method**

The format() method can be found on every string instance. It allows you to insert different values in positions within the string. This method works similarly to interpolation, save for the fact that you can't put expressions into the placeholders, and you have to pass in the values for insertion in the method call. The syntax for this is as follow;

**Example**

```python 
# Declaring a pie variables 

pie = 3

print("I ate some {} and it was yummy".format(pie))

name = "Jane Smith"
age = 30
salary = 12000

# We casting the number values to string since we are working with only string.
print("Hello there, My name is {}. i'm {} years old and my salary is ${}".format(name, str(age), str(salary)))

```


### **% Formatting**

An old, deprecated way of formatting strings, which you might end up seeing in old code, is the C language style % formatting. In this method, you use the % operator to pass in values. Inside the string, you use the % character, followed by a format specifier, to declare how the value should be inserted; for example, %s for string, or %d for integers:

**Example**

```python 



```

### **String Concatenation**

It’s very easy to use the `+ operator` for string concatenation. This operator can be used to add multiple strings together. However, the arguments must be a string. Here, The `+ Operator` combines the string that is stored in the number1 and number2 and stores in another variable result.


**Examples**

```python 
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

```