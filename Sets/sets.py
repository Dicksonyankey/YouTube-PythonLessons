#  ----    How to create sets in python ---------

# Creating a Set without  items.
web_broswers = {}

# creating set with items
web_broswers = {"Chrome", "FireFox", "MS Edge", "Brave"}
print(web_broswers)

# Creating a set of integers
numbers = set({1, 2, 3, 4, 5, 6, 7, 8})
print(numbers)

# Sets has no duplicates, let's demonstrate that.
names = {"Mick", "Mick", "Michael", "Trevor", "Trevor", "Franklin", "Mick"}
print(names)

# ---------------- Adding items using the add() method ---------------------
# Using the add() to add items into a sets
tech_companies = {"Google", "Facebook"}

tech_companies.add("Netflix")
tech_companies.add("Amazon")
tech_companies.add("Netflix")

print(tech_companies)


#  ---------  Updating items using the update() method -----------

cars = {"Toyata", "Volvo", "Ford"}
cars.update(["Mercedes", "BMW", "Kia"])
print(cars)


# ------------ using the len() to check the length of a set object.------------

# checking the length of cars
print(len(cars))

# checking the length of names
print(len(names))

# checking the length of tech_companies
print(len(tech_companies))


# ---------------  Removing items using the remove() method or discard() method  ---------

web_broswers = {"Chrome", "FireFox", "MS Edge", "Brave"}

# removing the item FireFox from the set
web_broswers.remove("FireFox")

# removing the item Brave from the set
web_broswers.remove("Brave")

# removing the item MS Edge from the set using discard()
web_broswers.discard("MS Edge")

print(web_broswers)


# ---------------  Using the clear() method to remove all items from the sets --------------

web_broswers = {"Chrome", "FireFox", "MS Edge", "Brave"}
print(web_broswers)

# using the clear method to empty the set.
web_broswers.clear()
print(web_broswers)


# -------------  Mathematical Notions on Set. --------------

# 1. Union() method

# Creating two sets.
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9, 10}

# Using the union method
new_set = set_a.union(set_b)
print(new_set)


# 2. Intersection() method

# Creating two sets.
set_a = {1, 2, 3, 4, 5}
set_b = {6, 1, 7, 8, 2, 3}

# Using the intersection method
new_set = set_a.intersection(set_b)
print(new_set)


# 3. difference() method

# Creating two sets.
set_a = {"Toyata", "Volvo", "Ford"}
set_b = {"Mercedes", "BMW", "Kia"}

# Using the difference method
# All elements of the 'set_a' set is returned except elements of the 'set_b'.
new_set = set_a.difference(set_b)
print(new_set)

# 4. issubset() method

# Creating two sets.
set_a = {1, 2, 3, 4}
set_b = {1, 2, 3, 4, 5, 6, 7}
set_c = {10, 11, 12, 13}

# Using the issubset method
new_set = set_a.issubset(set_b)
print(new_set)  # True

new_set1 = set_a.issubset(set_c)
print(new_set1)  # False


# 5. isdisjoint() method

# Creating two sets.
set_a = {"Toyata", "Volvo", "Ford"}
set_b = {"Mercedes", "BMW", "Kia"}
set_c = {"Volov", "BMW", "Kia"}

# Using the isdisjoint method
new_set2 = set_a.isdisjoint(set_b)
print(new_set2)  # True

new_set3 = set_a.isdisjoint(set_c)
print(new_set3)  # False
