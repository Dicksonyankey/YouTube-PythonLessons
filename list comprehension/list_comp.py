# ------  Example one --------
# creating an empty list
cube_list = []

# looping through values between the range of 0-9
for i in range(0, 10):
    # cubing them and appending them into a new list
    cube_list.append(i**3)
# printing the cube list
print(cube_list)


# In list comprehension
cube_list1 = [i**3 for i in range(0, 10)]
print(cube_list1)


# ------  Example two --------
# Let using the same example above for the case where we only append
# if the value is an Even number

cube_even = []
# looping through values between the range of 0-9
for i in range(0, 20):
    if i % 2 == 0:
    # cubing them and appending them into a new list
        cube_even.append(i**3)
# printing the cube list
print(cube_even)

# The list comprehension way
cube_even1 = [i**3 for i in range(0, 20) if i % 2 == 0]
cube_even1


# ------  Example three --------

# removing 0 from the new list
cube_even1 = []
for i in range(0, 20):
    if i % 2 == 0:
        if i == 0:
            continue
        cube_even.append(i**3)
print(cube_even)

# The list comprehension way
cube_even2 = [(i**3) for i in range(0, 20) if i % 2 == 0 and i != 0]
cube_even2

# ------  Example four --------

# Say we want the top earners from the employees dictionary in
# a tuple form.
employees = {
    'Alice': 100000,
    'Bob': 99817,
    'Carol': 122908,
    'Frank': 88123,
    'Eve': 93121
}

top_earners = [(key, val) for key, val in employees.items() if val >= 100000]
print(f"The Top {len(top_earners)} earners are {top_earners}")

