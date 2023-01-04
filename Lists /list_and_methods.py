# LIST DEFINITIONS
# A list is a data structure that holds an ordered collection of items i.e. we can store a sequence of items in a list. In Python, lists are created by placing all items within square brackets [] separated by comma.


# CREATING A LIST IN PYTHON
# It can have any number of items and they may be of different data types and can be created in the following manner:

# creating an empty list. 
list_a = []

print(list_a)

# creating a list with integers.
list_b = [1, 2, 3]
print(list_b)

# creating a list of names.
names = ["John","Jake","Drake","Smith","Sam"]
print(names)

# we can check the type of names variable to see they belong to a list data type
print(type(names)) # This is going to display <class 'list'>

# INDEXING IN PYTHON 

# indexing in programming starts from zero, so it is important to note that.
# by indexing i mean counting, so we also count in python starting from zero to N


# ACCESSING AN ITEM IN A LIST 
# we can access a list item by using the [] 
# creating a list of jobs 
list_of_jobs = ["Data Scientist", "Web Developer", "Hacker", "ML Engineer"]

# First of lets print the list 
print(list_of_jobs)


# let's access the first list in the list_of_jobs
print(list_of_jobs[0]) # this will display the first item in list.ie. "Data Scientist"
print(list_of_jobs[1]) # this will display the first item in list.ie. "Web Developer"
print(list_of_jobs[2]) # this will display the first item in list.ie. "Hacker"













# A list is a mutable sequence of zero, one, or more objects. A list can be modified using the builtin list methods such as append, insert, pop, and remove, etc. The order of the elements in a list can be updated using the methods, reverse and sort.
