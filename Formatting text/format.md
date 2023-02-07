# <u>Formatting Text In Python</u>

String formatting is important when you want to build new strings that are using existing values. Python provides several ways to format text strings. The most popular of these are formatted string, the `str.format()` method, and % formatting.


### **Formatted String**

 Formatted string  is the process of evaluating a string that has placeholders. These placeholders can hold expressions that yield a value, which is then placed inside the string. Special kinds of strings, known as `f-strings` is used during formatted string. These strings are prefixed with an f to denote how they're meant to be interpreted:

**Example**

```python 



```


### **The `str.format()` Method**

The format() method can be found on every string instance. It allows you to insert different values in positions within the string. This method works similarly to interpolation, save for the fact that you can't put expressions into the placeholders, and you have to pass in the values for insertion in the method call. The syntax for this is as follow;

**Example**

```python 
# Declaring a pie variables 

pie = 3

print("I ate some {} and it was yummy".format(pie))

```


### **% Formatting**

An old, deprecated way of formatting strings, which you might end up seeing in old code, is the C language style % formatting. In this method, you use the % operator to pass in values. Inside the string, you use the % character, followed by a format specifier, to declare how the value should be inserted; for example, %s for string, or %d for integers:

**Example**

```python 



```

### **String Concatenation**