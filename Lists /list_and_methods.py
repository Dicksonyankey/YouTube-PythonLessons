# ---------- LIST DEFINITIONS ------------

# A list is a data structure that holds an ordered collection of items i.e. we can store a sequence of items in a list. In Python, lists are created by placing all items within square brackets [] separated by comma.Moreover, the lists, due to their mutable nature, can be altered after their creation.We will talk more about list mutability.


# --------- CREATING A LIST IN PYTHON --------
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

# --------- INDEXING IN PYTHON ------------

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

# ------- LISTS MUTABILITY IN PYTHON ----

# List mutability in Python means that one can change an item present in a list by accessing it directly as part of the assignment statement. However, one can update one of the list items by using the indexing operator on the left side of an assignment.

# Creating a list of cars
list_of_cars = ["Toyoto","Mercedes","Ford","Jeep","Audi","BMW"]

# Altering changes after creation : changing Mercedes to Kia
list_of_cars[1] = "Kia"

# Altering changes after creation : changing Toyota to Volvo
list_of_cars[0] = "Volvo"

# dispplay the list of cars to see the changes
print(list_of_cars)


# -------- LIST SLICING IN PYTHON -----------
# We can equally slice a list alos using the square bracket [],but the bracket will have a accept some kind of parametersand a colon. that's 1. start 2. stop and 3. step that's [start:stop:step] . i want to mention that the stop is with -1

# slicing the sub element from the list of cars : i want to select from index 0-3
new_cars = list_of_cars[0:3]
print(new_cars)


# slicing the last 3 cars from the list of cars.
last_three = list_of_cars[3:]
print(last_three)


# --------- STORING DIFFERNENT TYPE OF DATA IN A LIST-----------
#List can store different data type such as int, float, string, dictionary and list itself.

# creating a list that stores different data types 
diff_list = [1, 3.14, 3, "python",[1,22,3.0],{"name":"Mr Jake"}]

print(diff_list) # This will display the list 


# ------- TRAVERSING A LIST --------- 
# We traverse a list using for loop in pthon ie. using the for keyword.let's look at some examples.

# we will traverse the diff_list items 
for item in diff_list:
    # the print item will display all the items in the list line by line in the 
    # order it starts in the diff_list.
    print(item)


# also we can use the enumerate() to traverse through the list 
# to have access to the index,item in the list.
for index,item in enumerate(diff_list):
    print(f"{index}. {item}")


# ----- LIST OPERATIONS -----
# 1. we can user the + operator on two list ie. it will join/concatenate these two list.
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]

list_3 = list_1 + list_2
print(list_3)

# 2.similarly, the * operator repeats a list a given number of times

ones = [1] * 5
print(ones)

zeros = [0] * 10
print(zeros)

# -----  LIST METHODS -----

# A list can be modified using the builtin list methods such as append, insert, pop, and remove, etc. The order of the elements in a list can be updated using the methods, reverse and sort which will be discussed next.

# 1. append(element) -> Used for appending and adding elements to the end of the List.
# 2. extend(list) -> Adds each element of the iterable to the end of the List
# 3. insert(index, element) -> Inserts a given element at a given index in a list.
# 4. count(element) -> This methods count the elements
# 5. index(element) -> Returns the lowest index where the element appears.
# 6. pop(element) -> Removes and returns the last value from the List or the given index value.
# 7. remove(element) -> Removes a given object from the List.
# 8. sort() -> Sort a List in ascending, descending.
# 9. reverse() -> Reverses objects of the List in place.
# 10. clear() -> This method is used for removing all items from the list.
# 11. copy() -> It returns a shallow copy of a list
# shallow copy create a copy of that object but reference each element differently.
# deepcopy creates a copy of the object and the elements in that object















# sample 1
list_1 = [1, 2, 3, 4, 5]
new_list = list_1

new_list[0] = 100
print(list_1)
print(new_list)

print("The id of list_1", id(list_1))
print("The id of new_list", id(new_list))

# sample 2
list_2 = [[1, 2], [3, 4],[5,6] ]
new_list1 = list_2.copy()
new_list1[0] = ["a","b"]

print(list_2)
print(new_list1)

# sample 3
list_3 = [[1, 2], [3, 4], [5, 6]]
new_list2 = list_3.copy()
new_list2[0][1] = "a"

print(list_3)
print(new_list2)
