#A dictionary is a built in Python data type that stores data as key value pairs
#It is defined using cury braces {}
#Each key maps to exactly one value, keys ust be unique and immutable

#syntax
'''
dictionary_name = {key1: value1,
                   key2: value2,
                   key3: value3
                   }
'''

student = {
    "name" : "Ashley",
    "Program" : "Computer Science",
    "Age" : 24,
    "marks": 89
}
#Accessing dictionary data
print(student["Program"])
print(student.get("Age"))
print(student.get("CGPA")) #Returns None even item does not exist
#print(student["CGPA"]) # Returns an error as item not found

#Updating Dictionary Data
student["Age"] = 100
print(student.get("Age"))

student["school"] = "Computer Applications"
print(student)

student.update({"Attendance": "90%", "Roll No":"11"}) #Bulk updating
print(student)

#Deleting Dictionary Items
del student["name"] #removes the specified key
print(student)
print(student.pop("Age")) #Removes and returns the value 
#student.clear() #Empties the entire dictionary
print(student)

#Dictionary Functions
#keys
print(student.keys()) #Returns of the dictionary keys as a view

#Values
print(student.values()) #Returns all the dictionary values as a view

#Items
print(student.items()) #Returns all the dictionary items(both key and value) as a tuple

#Searching Key in dictionary
for key in student.keys():
    if key == "Attendance":
        print("Key Exists")
        break
#Searching Value in Dictionary
for value in student.values():
    if value == "Ashley":
        print("Value found")
        break
#Searching using items()
for key, value in student.items():
    if value == "Computer Applications":
        print("Value found at key : ", key)
        break


