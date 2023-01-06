# -----------   Tuples in python -----------

# Tuples are immutable and fixed size, Python allocates just the minimum memory block required for the data. As a result, tuples are more memory efficient than the lists.

# --------- How to create a tuple -----------
# tuples are created using the parenthesis () and each element or item is separated by comma.
# But first let's understand that, tuples can be created in two way
# 1. with the parenthesis ie. () 2. wtth the tuple built-in function ie. tuple()

# let's create a tuple in python
point = (5, 7)  # this is a tuple containing points
print(point)

numbers = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9))  # this is a tuple of numbers
print(numbers)


# --------- Tuples containing different data types  -----------
# here we clearly see that the tuples contains different kinds of data, ie. string, integers, float and a list
mixed_dtype = tuple(("Python", "Javascript", 1, 2,
                    3, 34.56, 78.90, [1, 2, 3, 4]))
print(mixed_dtype)
print(type(mixed_dtype))  # checking the type of the data -> <class "tuple">


# --------- How to convert other data type into a tuple ------------
# converting a lisst into a tuple.
names = ["Smith", "Jane", "Ronny", "Michael", "Franklin", "Trevor"]
list_to_tuple = tuple(names)
print(list_to_tuple)
print(type(list_to_tuple))


# converting a string into a tuple.
word = "PythonProgramming"
letters = tuple(word)
print(letters)
print(type(letters))


# converting a dictionary into a tuple.
# The output of this will surprice you a little because once the tuple function has been applied on the dictionary we should automatically get the dict converted to tuple. if you know about dictionaries already  what will happen is that, you will only get the keys in the dictionary.

# like this output -> ('name', 'age', 'job', 'salary') instead of (('name', 'Trevor'), ('age', 34), ('job', 'Ml Engineer'), ('salary', 1225000))

person_info = {"name": "Trevor", "age": 34,
               "job": "Ml Engineer", "salary": 1225000}
dict_to_tuple = tuple(person_info)
print(dict_to_tuple)  # output -> ('name', 'age', 'job', 'salary')

# To fix the problem and achieve the (('name', 'Trevor'), ('age', 34), ('job', 'Ml Engineer'), ('salary', 1225000)) output, we need to add the items() method on the dictionary.
dict_to_tuple1 = tuple(person_info.items())
print(dict_to_tuple1)


# --------- Slicing a sub element from a tuple ------------
names = ("Smith", "Jane", "Ronny", "Michael", "Franklin", "Trevor")
print(names[2:4])
print(names[0:3])


# --------- Traversing a tuple ------------
names = ("Smith", "Jane", "Ronny", "Michael", "Franklin", "Trevor")
for name in names:
    print(name)


for detail in dict_to_tuple1:
    print(detail)


# --------- Tuple methods  ------------
# There are only two methods on the tuple object, and they are index(x) and count(x)
tuple_num = (1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5,)


# Counting the number of ones usinf the count(x) method. 
print(tuple_num.count(1))
print(tuple_num.count(2))
print(tuple_num.count(4))


# Checking the index using the index(x) method.
# Here we have multiple occurance of 1 , 2 and 4. so python will pick just the first occurance.
print(tuple_num.index(1))
print(tuple_num.index(2))
print(tuple_num.index(4))
print(tuple_num.index(5))


# -------- The difference between tuple and list -----------
# Lists are mutable, Python needs to allocate an extra memory block in case there is a need to extend the size of the list object after it is created. However tuples are immutable and are fixed. if they are initialized and created, elements in the tuple can not be altered or changed.


# ---------- Main Takeaway ---------
# 1. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected and will not accidently change.
# 2. Tuple doesn't not also support data updating or changing the state once it is created
# 3. use list if you know that the data will grow and shrink during the runtime of the application,you need to go with the list data type.
