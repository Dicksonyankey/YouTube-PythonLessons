# Dictionaries are data types in python that which allows data to be stored in a key-value-pair format.



# DICTIONARY COMPREHENSION 

# dictionary comprehension is a cool and elegant way that helps us to create a dictionary.


# Example one 

def create_dict(start, stop):
    cube_dict = {}
    for num in range(start,stop):
        cube_dict[num] = num ** 3
    return cube_dict


# Now let's solve this same problem using the comprehension
cube_dict1 = {num:num ** 3 for num in range(1,11)}


# Example two
car_prices = {"Volvo":230000, "Toyota":150000, "Mercedes":340000, "Ford":200000}

# using functions to update the car prices 
def update_car_price(car_object):
    new_prices = {}
    increase_rate = 2.43
    for key, value in car_object.items():
        new_prices[key] = value * increase_rate
    return new_prices

# We want to use comprehension to update the car price 
new_prices = {key:value * 2.43 for key, value in car_prices.items()}


if __name__ == "__main__":
    # print(create_dict(1,11))
    # print(cube_dict1)
    print(update_car_price(car_prices))
    print(new_prices)
    
    


