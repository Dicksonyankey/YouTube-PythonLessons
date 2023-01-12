There are two ways of creating a dictionary:

`my_dictionary = dict()`

`my_dictionary2 = {}`

1. A dictionary is a collection of key-value pair
2. and the value of a dictionary can be accessed by the key
3. the keys are the left hand side and the values are the right hand side
4. to print data you do `print(name_of_dictionary['key_name'])`


```python
my_dict = dict({"name":"Python", "age": 20, "type": "Fun"})
print(my_dict) # {'name': 'Python', 'age': 20, 'type': 'Fun'}

```


```python
print(my_dict["name"]) # Python
print(my_dict["age"]) # 20
print(my_dict["type"]) # Fun
```


```python 

python = {
    "firstName": "Python",
    "lastName":"programming language",
    "age":30,
    "areas":["Data Science", "Mobile App", "Web App"]
}

print(python)
print(python["firstName"])
print(python["lastName"])
print(python["areas"][1:])

```

# Dictionaries Methods

```
PYTHON DICTIONARY METHODS
METHOD	      DESCRIPTION
clear()	      Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys()	  Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist:insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary

```

```python 

student_data = {
  "name":"Jane Smith",
  "age":21,
  "degrees":['Bsc Computer Science',"MSc", "PDH",{
      "hobbies":["video game","reading","dancing",{
          "car":{
              "name":"Toyota",
              "year": 2020,
              "color":"Black"
          }
      }]
  }]
}

# Using the square bracket to also get items
print(student_data["degrees"][3]["hobbies"][3]["car"]["color"])


# Using the get method to so get items from the ductionary.
print(student_data.get("degrees")[3].get("hobbies")[3].get("car").get("color"))

```


#### Methods 

```python
# get 
# ["key"]
print(student_data["name"])
print(student_data.get("name"))


# keys()
print(student_data.keys())

# values()
print(student_data.values())


# pop()
print(student_data.pop("name"))


print(student_data)


# popitem()
print(student_data.popitem())


```