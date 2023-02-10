import csv
import json


f = open("my_text.txt", "w")
f.write("Hello world, i live coding.")
f.close()


f = open("my_text.txt", "a")
f.write("i wanted to write love and not live.")
f.close()


f = open("my_text.txt", "r")
print(f.read())
f.close()


f = open("my_text.txt", "a")
f.write("\ni wanted to write love and not live.")
f.close()


f = open("my_text.txt", "w")
f.write("Hello there, my name is python programming, and i am 30 years old since i was\nfirst created by Van.")
f.close()



f = open("my_text.txt", "r")
print(f.readlines())
f.close()


# --------------------- The with Context Manager ---------------------

# The readline will return the first line of the data as a string.
with open("my_text.txt", "r") as f:
    data = f.readline()
    print(data)
    print(type(data))




# The readlines returns the data as a list
with open("my_text.txt", "r") as f:
    data = f.readlines()
    print(data)
    print(type(data))




# The read return the data as string.
with open("my_text.txt", "r") as f:
    data = f.read()
    print(data)
    print(type(data))




with open("my_text.txt", "r") as f:
    # Seek help move the cursor to a specific position in the file
    f.seek(13)
    # Tells you the length of the sets Reference point
    length = f.tell()
    data = f.read()
    print(length)
    print(data)


# Reading a binary text file 
with open("binary.txt", "rb+") as f:
    # the binary file needs to be converted into a string. 
    data = f.read().decode("utf-8")
    # display that data in the file 
    print(data)


with open("employee.csv","r") as f:
    csv_data = csv.reader(f)
    print(csv_data)
    
    data = [row for row in csv_data]
    print(data)



with open("employee.csv","r") as f:
    csv_data = csv.reader(f)
    
    line = 1
    for row in csv_data:
        if line > 1:
            print(row)
        line += 1



with open("employee.csv","w") as f:
    cvs_writer = csv.writer(f)
    cvs_writer.writerow(["peter smith",37,99000,"M","Sales","G4",709])
    cvs_writer.writerow(["Jane Doe",24,129000,"F","Accouting","G1",520])



with open("people.csv", "w") as f:
    fields = ["Name", "Age", "Salary"]
    people_writer = csv.DictWriter(f, fieldnames = fields)
    
    # Writing the fields as the first row
    people_writer.writeheader()
    
    # Adding the corresponding data
    people_writer.writerow({"Name": "Micheal Ackah", "Age": 25, "Salary": 120000})
    people_writer.writerow({"Name": "Janet Ackah", "Age": 20, "Salary": 90000})
    people_writer.writerow({"Name": "Peter johnson", "Age": 67, "Salary": 1200000})



sample = {
    "name" : "Peter Amanfo",
    "Age" : 34
}

json_sample = json.dumps(sample)
print(json_sample)
print(type(json_sample))


original_sample = json.loads(json_sample)
print(original_sample)
print(type(original_sample))