# 1. Accept a sentence and display its unique vowels and their count.
# sentence = input("Enter a sentence : ").lower()
# vowels = set()

# for character in sentence:
#     if character in "aeiou":
#         vowels.add(character)

# print("Unique vowels : ", vowels)
# print("Count : ", len(vowels))

#b. Given A = {1,2,3,4,5} and B = {4,5,6,7} 

# A = {1,2,3,4,5}
# B = {4,5,6,7}
# print("A Union B : ", A.union(B))
# print("A Intersection B : ",A.intersection(B))
# print("A difference B : ", A.difference(B))
# print("A symmetric Difference : ", A.symmetric_difference(B))

# A.update(B)
# print("Updated set A : ", A)

#Question 2
stock = {"pen" : 10,
         "book" : 5,
         "bag" : 2
        }
stock.update({"pencil" : 25})
stock["book"] = 8
stock.pop("bag")

print(stock)

#b 
d1 = {"a": 10, "b":20, "c":30}
d2 = {"b": 5, "c":15, "d":40}
d3 = {}
d3.update({d1, d2})
print("Merged dictionary : ",d3)