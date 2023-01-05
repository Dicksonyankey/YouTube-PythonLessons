# Dictionaries are data types in python that which allows data to be stored in a key-value-pair format.


# DICTIONARY COMPREHENSION

# dictionary comprehension is a cool and elegant way that helps us to create a dictionary.
# Example one

def create_dict(start, stop):
    cube_dict = {}
    for num in range(start, stop):
        cube_dict[num] = num ** 3
    return cube_dict


# Now let's solve this same problem using the comprehension
cube_dict1 = {num: num ** 3 for num in range(1, 11)}

# Example two
car_prices = {"Volvo": 230000, "Toyota": 150000,
              "Mercedes": 340000, "Ford": 200000}

# using functions to update the car prices
def update_car_price(car_object):
    new_prices = {}
    increase_rate = 2.43
    for key, value in car_object.items():
        new_prices[key] = value * increase_rate
    return new_prices


# We want to use comprehension to update the car price
new_prices = {key: value * 2.43 for key, value in car_prices.items()}


# COMPREHENSION WITH IF STATEMENTS
# we want to filter through the list of dictionaries for the salaries above 100,000
workers = [
    {"name": "Jack", "salary": 100000},
    {"name": "John", "salary": 120000},
    {"name": "smith", "salary": 130000},
    {"name": "Micky", "salary": 90000}
]

# Using functions to solve the problem

def filter_salary(dict_object):
    high_salary = {}
    for item in dict_object:
        if item["salary"] > 100000:
            high_salary[item["name"]] = item["salary"]
    return high_salary


# Let's now use the list comprehension for the same problem
filter_salary2 = {item["name"]: item["salary"]
                  for item in workers if item["salary"] > 100000}

# comprehension with multiple if statements : but lets change smith salary to 133333
filter_salary3 = {item["name"]: item["salary"]
                  for item in workers if item["salary"] > 100000 if item["salary"] % 2 == 0}

if __name__ == "__main__":
    # print(create_dict(1,11))
    # print(cube_dict1)
    print(update_car_price(car_prices))
    print(new_prices)
    print(filter_salary2)
    print(filter_salary3)

# MAIN TAKEAWAY
# using dict comprehension shorten the process of initializing a dictionary
# and it also make your code pythonic and reable ans intact
# it also makes you reduce the amount of code you write.
