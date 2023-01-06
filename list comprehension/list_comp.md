## List Comprehension

List comprehension is an elegant way to define and create a list in Python. It is used to create a new list in a single line. Consider the following examples below:

```python

for item in sequence:
    if condition:
        output expression
```

The code above can be written as:

```python
# This is what we call the list comprehension
[output expression for item in sequence if condition]

```

### Exercise
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted', 'Safari', 'corrupted',
'Safari', 'corrupted', 'Chrome', 'corrupted', 'Firefox', 'corrupted']

In the visitors lists, there are `courrupted` items. Try to convert the corrupted elements or items in the list to the item that comes before it in the list.

**output**
['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari', 'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox'] 

visit the `solution.py` for the code to the exercise.
visit the `list_comp.py` file for examples. Thank you.
