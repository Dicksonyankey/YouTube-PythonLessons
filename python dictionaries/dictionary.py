my_dict = dict({"name": "Python", "age": 20, "type": "Fun"})
print(my_dict)  # {'name': 'Python', 'age': 20, 'type': 'Fun'}


print(my_dict["name"])  # Python
print(my_dict["age"])  # 20
print(my_dict["type"])  # Fun

python = {
    "firstName": "Python",
    "lastName": "programming language",
    "age": 30,
    "areas": ["Data Science", "Mobile App", "Web App"]
}

print(python)
print(python["firstName"])
print(python["lastName"])
print(python["areas"][1:])


# Dictionaries methods


student_data = {
    "name": "Jane Smith",
    "age": 21,
    "degrees": ['Bsc Computer Science', "MSc", "PDH", {
        "hobbies": ["video game", "reading", "dancing", {
            "car": {
                "name": "Toyota",
                "year": 2020,
                "color": "Black"
            }
        }]
    }]
}

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
