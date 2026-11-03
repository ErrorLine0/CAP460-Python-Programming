# A set in Python is a collection data type that stores unique items(no duplicates)
# It is unordered (noindexing) and is mutable (items can be added removed after declaration)

#Syntax
'''
setname = {items}
'''
#Testing if it store duplicate items
marks = {10,80,10,20,70}
print(marks) #Returns only one 10 removes the other 10

fruits = {"apple","orange","cherry","mango","guava"}

#Accessing set items by looping
for item in fruits:
    print(item)

#Using index
#print(fruits[0]) #Error as sets do not support indexing

#Checking membership
print("apple" in fruits) #Returns True as applie is a member of the set
print("banana" in fruits) #Returns False as banana does not exist in the set


#Set Opperations
#Adding items
fruits.add("banana") #adding single item
fruits.update(["grapes","lemon","peach"]) #bulk adding
print(fruits)

#Remove Operations
fruits.remove("apple") #Removes the item apple from the set
print(fruits)
fruits.discard("orange")
print(fruits)

#fruits.remove("apple") #Trying to remove an non existing element will return an error
fruits.discard("apple") #using Discard will not return an error even when item does not exist
print(fruits)

#Set comprehension
numbers = {1,2,3,4,5}
squares = {n**2 for n in numbers}
print(squares)
#doing the same above squres set but using for loop
squares2 = set()
type(squares2)
for item in numbers:
    squares2.add(item**2)
print(squares2)
"""
Observation notice:
Initially, I used squares2 = {} to create an empty set,
but encountered an error when trying to add elements.

After checking its type using type(squares2), I discovered
that Python interprets {} as an empty dictionary.

To create an empty set, we must use set() instead.
"""
