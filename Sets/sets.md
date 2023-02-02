## <u>SETS IN PYTHON</u>

**What you will learn**
### 1. what is python sets?
A set is an unordered and unindexed collection of items. It is a collection data type which is mutable, iterable and contains no duplicate values.

**Note**: 
i. A set in Python represents the mathematical notion of a set.

ii. Once a set set is created, we cannot change its items, but we can add new items using the add() method.


### 2. How to create sets in python
1. **using {}**
```python 
# Creating a Set without  items.
web_broswers = {}

# creating set with items 
web_broswers = {"Chrome", "FireFox","MS Edge", "Brave"}
print(web_broswers)
```

2. **using set() built-in function**
```python
# Creating a set of integers
numbers  = set({1,2,3,4,5,6,7,8})
print(numbers)

# Sets has no duplicates, let's demonstrate that.
names = {"Mick","Mick","Michael","Trevor","Trevor","Franklin","Mick"}
print(names)
```
### 3. Why set doesn't support slicing? 

slicing sets does not work because, We cannot access items in a set by referring to an index (slicing operation), since sets are unordered the item has no index. 

### 4. Adding items using the add() method
Python won’t add the same item again nor will it throw any error.

```python
# Using the add() to add items into a sets
tech_companies = {"Google", "Facebook"}

tech_companies.add("Netflix")
tech_companies.add("Amazon")
tech_companies.add("Netflix")

print(tech_companies)
```

### 5. Adding multiple items using the update() method
In order to add multiple items, we use the update() method with new items to be added within a list.

```python
cars = {"Toyata", "Volvo", "Ford"}
cars.update(["Mercedes", "BMW", "Kia"])
print(cars)
```


6. using the len() to check the length of a set object.
```python
# checking the length of cars
print(len(cars))

#checking the length of names
print(len(names))

# checking the length of tech_companies
print(len(tech_companies))
```

7. Removing items using the remove() method or discard() method
If we try to remove an item using the remove() which is not present in the set, Python will throw an error.
```python
web_broswers = {"Chrome", "FireFox","MS Edge", "Brave"}

# removing the item FireFox from the set
web_broswers.remove("FireFox")

# removing the item Brave from the set
web_broswers.remove("Brave")

# removing the item MS Edge from the set using discard()
web_broswers.discard("MS Edge")

print(web_broswers)
```

8. Using the clear() method to remove all items from the sets
We use the clear() method to empty the set.

```python
web_broswers = {"Chrome", "FireFox","MS Edge", "Brave"}
print(web_broswers)

# using the clear method to empty the set.
web_broswers.clear()
print(web_broswers)
```

### 9. Mathematical Notions on Set.
- **Union() method**
This method allows performing a union between sets. This operation returns all elements within both sets.

```python
# Creating two sets.
set_a = {1,2,3,4,5} 
set_b = {6,7,8,9,10}

# Using the union method
new_set = set_a.union(set_b)
print(new_set)
```

- intersection() method
This method performs the intersection be- tween sets. It returns only elements which are available in both sets.

```python
# Creating two sets.
set_a = {1,2,3,4,5} 
set_b = {6,1,7,8,2,3}

# Using the intersection method
new_set = set_a.intersection(set_b)
print(new_set)
```

- difference() method
This method performs the difference opera- tion and returns a set containing all elements of the calling object but not including elements of the second set.

```python
# Creating two sets.
set_a = {"Toyata", "Volvo", "Ford"} 
set_b = {"Mercedes", "BMW", "Kia"}

# Using the difference method
# All elements of the 'set_a' set is returned except elements of the 'set_b'.
new_set = set_a.difference(set_b)
print(new_set)
```

- issubset() method
This method checks whether all elements of calling set is present within a second set or not. It returns true if the calling set is subset of the second set, false otherwise.


```python
# Creating two sets.
set_a = {1,2,3,4} 
set_b = {1,2,3,4,5,6,7}
set_c = {10,11,12,13}

# Using the issubset method
new_set = set_a.issubset(set_b)
print(new_set) # True

new_set1 = set_a.issubset(set_c)
print(new_set1) # False
```

- isdisjoint() method
This method checks for the intersection be- tween two sets. It returns true if the calling set is disjoint and not intersected with the second set, false otherwise.

```python
# Creating two sets.
set_a = {"Toyata", "Volvo", "Ford"} 
set_b = {"Mercedes", "BMW", "Kia"}
set_c = {"Volov", "BMW", "Kia"}

# Using the isdisjoint method
new_set2 = set_a.isdisjoint(set_b)
print(new_set2) # True

new_set3 = set_a.isdisjoint(set_c)
print(new_set3) # False

```

### 10. Main takeaway

1. Sets are unindexed and unordered collection of item which does not acccepts duplicates.
2. As sets are unindexed and unordered, you cannot slice items from them.
3. Once Sets are created you cannot change its items but we can add items into the set.


