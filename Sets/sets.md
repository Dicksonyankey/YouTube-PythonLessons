## <u>SETS IN PYTHON</u>

**What you will learn**
1. what is python sets?
A set is an unordered and unindexed collection of items. It is a collection data type which is mutable, iterable and contains no duplicate values.

**Note**: 
i. A set in Python represents the mathematical notion of a set.

ii. We cannot access items in a set by referring to an index (slicing operation), since sets are unordered the item has no index. 

iii. Once a set set is created, we cannot change its items, but we can add new items using the add() method.

2. How to create sets in python
    - using {}
```python 
# Creating a Set without  items.
web_broswers = {}

# creating set with items 
web_broswers = {"Chrome", "FireFox","MS Edge", "Brave"}
print(web_broswers)
```

    - and using set() built-in function
```python
# Creating a set of integers
numbers  = set({1,2,3,4,5,6,7,8})
print(numbers)

# Sets has no duplicates, let's demonstrate that.
names = {"Mick","Mick","Michael","Trevor","Trevor","Franklin","Mick"}
print(names)
```
3. Why set doesn't support slicing? 
slicingin sets does not work because, sets are unordered and unindexed data type.Once a set set is created, we cannot change it's items, but we can add new items using the add() method.

4. Adding items using the add() method
5. Adding multiple items using the update() method
6. using the len() to check the length of a set object.
7. Removing items using the remove() method
8. Using the clear() method to remove all items from the sets
9. Mathematical Notions on Set.
    - Union() method
    - intersection() method
    - difference() method
    - issubset() method
    - isdisjoint() method
    - issuperset() method
    
10. Main takeaway