# Sequence Types

# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#! Lists
# TODO Creating Lists
# 1. ✅ Create a list of 10 pet names
# The code snippet you provided is creating a list of pet names. The
# list contains 10 pet names: "Rose", "Meow Meow Beans", "Mr.Legumes",
# "Luke", "Lea", "Princess Grace", "Spot", "Tom", "Mini", and "Paul".
# This list can be accessed and manipulated using various list
# operations and methods in Python.
pet_names = [
    "Rose",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Luke",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
]

pet_names2 = ["Toby", "Mikey"]

# TODO Reading Information From Lists
# 2. ✅ Return the first pet name
# print(pet_names[0])
# 3. ✅ Return all pet names beginning from the 3rd index (included)
# for i in range(3, len(pet_names)):
#     print(pet_names[i])
# print(pet_names[3:])
# 4. ✅ Return all pet names before the 3rd index (not included)
# print(pet_names[:3])
# 5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index
# print(pet_names[3:8])
# 6. ✅ Find the index of a given element
# print(pet_names.index("Rose")) #=> raises a ValueError if not present
# 7. ✅ Read the original list in reverse order
#!DESTRUCTIVE vs NON_DESTRUCTIVE
# print(pet_names.reverse()) # => DESTRUCTIVE
# print(pet_names[::-1])  # => NON DESTRUCTIVE
# 8. ✅ Return the frequency of a given element
# print(pet_names.count("Rose"))

# TODO Updating Lists
# 9. ✅ Change the first pet_name to all uppercase letters
# pet_names[0] = pet_names[0].upper()
# 10. ✅ Append a new name to the list
# pet_names.append("Toby")
# 11. ✅ Add a new name at a specific index
# pet_names.insert(1, "Mikey")
# 12. ✅ Add two lists together
# print(pet_names + pet_names2) # NON DESTRUCTIVE
# pet_names.extend(pet_names2) # DESTRUCTIVE
# 13. ✅ Remove the final element from the list
# print(pet_names.pop())  # gives back the popped element, DESTRUCTIVE!!!!
# print(pet_names)
# 14. ✅ Remove element by specific index
# print(pet_names.pop(2))
# 15. ✅ Remove a specific element
# pet_names.remove("Bob")  # Raises ValueError if the value is not present
# 16. ✅ Remove all pet names from the list
# print(pet_names.clear()) # DESTRUCTIVE
# print(pet_names)

#!Tuple
# 📚 Review:
# Mutable, Immutable <=> Changeable, Unchangeable

# Why Are Tuples Immutable?

# What advantages does this provide for us? In what situations
# would this serve us?
# Can I mutate the content of a tuple if the element is a list/dict (a mutable Data Structure)?

# TODO Accessing Elements
# 17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages
empty_tuple = ()
single_tuple = (True,)
ages_generator = tuple(range(10))

# 18. ✅ Print the first pet age
# print(ages_generator[9])

# TODO Testing Mutability (you can add a tuple to a tuple though)
# 19. ✅ Attempt to remove an element with ".pop" => AttributeError: 'tuple' object has no attribute 'pop'
# 20. ✅ Attempt to change the first element #=> TypeError: 'tuple' object does not support item assignment

# TODO Tuple Methods
# 21. ✅ Return the frequency of a given element
# print(ages_generator.count(3))
# 22. ✅ Return the index of a given element
# print(ages_generator.index(3))

#! Range
# 23. ✅ create a Range
# Note:  Ranges are primarily used in loops
# list_ten_thousand = list(range(10000))
# for i in range(len(pet_names)):
#     print("Hello world!")

#! Sets (value cannot be modified but you can add/remove elements)
# 24. ✅ Create a set of 3 pet foods
pet_fav_food = {"house plants", "fish", "bacon"}
# print("🚀 ~ pet_fav_food:", pet_fav_food)

# TODO Reading
# 25. ✅ Print set elements with a loop
# for el in pet_fav_food:
#     print(el)
# 26. ✅ Check if an element is in a set
# print("house plant" in pet_fav_food)
# 27. ✅ Get first element
#! not possible, a set is not ordered!!!
# 28. ✅ Get a copy of a set
# copy = pet_fav_food.copy()
# print(copy)
# 29. ✅ isdisjoint, issubset, issuperset
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# TODO Updating
# 30. ✅ Add an element to a set
# set1.add(4)
# 31. ✅ Union, intersection, difference
# set1.intersection(set2) #=> {3} and it's COMMUTATIVE
# set1.isdisjoint(set2) #=> False because {3} in common
# set1.difference(set2) #=> {1, 2} and it's NOT COMMUTATIVE can also use "-"
# set1.union(set2) #=> {1, 2, 3, 4, 5} and it's NOT COMMUTATIVE
# 32. ✅ Update current set with elements from other set
# set1.update(set2)

# TODO Deleting
# 33. ✅ Delete specific el using ".remove"  VS ".discard"
# pet_fav_food.remove("baconS") #=> removes the el if present, else KeyError
# pet_fav_food.discard("baconS")  # => removes the el if present, else nothing is done
# # 34. ✅ Delete random element using ".pop"
# pet_fav_food.pop()

#! Dictionaries (from 3.7+, dictionaries are ordered)
# TODO Creating
# 35. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {"name": "Rose", "age": 11, "breed": "domestic long"}
# 36. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name="Spot", age=25, breed="boxer")

# TODO Reading
# 37. ✅ Print the pet attribute of "name" using bracket notation
# print(pet_info_rose["nameS"]) #! watch out for keyErrors when asking for a key that doesn't exist
# 38. ✅ Print the pet attribute of "age" using ".get"
# print(pet_info_rose.get("nameS", False)) #! watch out for keyErrors when asking for a key that doesn't exist

# Note: ".get" is preferred over bracket notation in most cases
# because it will return "None" instead of an error
# 39b. ✅ Get dict keys
# print(pet_info_rose.keys())
# # 39c. ✅ Get dict values
# print(pet_info_rose.values())
# 39d. ✅ Get dict pairs
# print(pet_info_rose.items())

# TODO Updating
# 40. ✅ Update Rose's age to 12
# pet_info_rose["age"] += 1
# print(pet_info_rose)
# 41. ✅ Update Spot's age to 26

# TODO Deleting
# 42. ✅ Delete Rose's age using the "del" keyword => []
# del pet_info_rose["age"] #=> KeyError if key/value pair is not present
# print(pet_info_rose)
# 43. ✅ Delete Spot's age using ".pop"
# pet_info_rose.pop("age", False)  # => Nothing is done if key/value pair is not present, can provide a default
# 44. ✅ Delete the last item for Rose using "popitem()"
# pet_info_rose.popitem()
# print(pet_info_rose)
# 45 ✅ Delete every key/value pair => clear()
# print(pet_info_rose.clear())
# print(pet_info_rose)

#! Loops
pet_info = [
    {
        "name": "Rose",
        "age": 11,
        "breed": "domestic long-haired",
    },
    {
        "name": "Spot",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Gracie",
        "age": 2,
        "breed": "domestic long-haired",
    },
]

# 46. ✅ Loop through a range of 10 and print every number within the range
# 47. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# 48. ✅ Loop through the "pet_info" list and print every dictionary
# i = 0

# while i < len(pet_names):
#     print(pet_names[i])
#     i += 1

# for i, pet in enumerate(pet_names):
#     print(f"{i+1}. {pet}")

#! Exercises for you to practice
# 49. ✅ Create a function that takes a list a parameter
# The function should use a "for" loop to loop through the list and print each item
# Invoke the function and pass it "pet_names" as an argument
# 50. ✅ Create a function that takes a list as a parameter
# The function should define a variable ("counter") and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Once the loop has finished, return the final value of "counter"
# 51. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dictionaries", "name" and "age" as parameters
# Create an index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param
# and the index is less then the length of the list
# Every list will increase the index by 1
# If the dictionary containing a matching name is found, update the item's age with the new age
# Otherwise, return 'Pet not found'

#! Functional Programming corner
# map like VS map
# 52. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
#! WAY 1 -> the manual way
# final = []
# for pet_name in pet_names:
#     final.append(pet_name.upper())
# print(final)
#! WAY 2 -> the comprehension way
# print([pet_name.upper() for pet_name in pet_names])
#! WAY 3 -> the map() way
# print(list(map(lambda pet_name: pet_name.upper(), pet_names)))

# find like VS find
# 53. ✅ Use list comprehension to find a pet named spot
# for pet_dict in pet_info:
#     if pet_dict["name"] == "Spot":
#         print(pet_dict)

print(next((pet_dict["name"] for pet_dict in pet_info if pet_dict["age"] < 2), None))

# filter like VS filter
# 54. ✅ Use list comprehension to find all of the pets under 3 years old
# print([pet_dict["name"] for pet_dict in pet_info if pet_dict["age"] < 3])
# print(list(filter(lambda pet_dict: pet_dict["age"] < 3, pet_info)))

# reduce like VS reduce
# 55. ✅ Use list comprehension to find all of the pets under 3 years old

#! Writing Generators
# 56. ✅ Create a generator expression matching the filter above
# gen_exp = (pet_name.upper() for pet_name in pet_names)
# import ipdb; ipdb.set_trace()

#! Compare Generators and Expressions
import sys
import timeit

starter_list = list(range(100000))

#! MEMORY
# print(
#     "List Comprehension Memory Size",
#     sys.getsizeof([el for el in starter_list if el % 2 == 0]),
# )
# # 444376
# print(
#     "Generator Expression Memory Size",
#     sys.getsizeof((el for el in starter_list if el % 2 == 0)),
# )
# 208

#! RUNTIME
# print(
#     "Comprehension Run 1 Time",
#     timeit.timeit(
#         "[el for el in starter_list if el%2==0]",
#         "from __main__ import starter_list",
#         number=1,
#     ),
# )
# # => 0.005183833185583353
# print(
#     "Comprehension Run 1000 Time",
#     timeit.timeit(
#         "[el for el in starter_list if el%2==0]",
#         "from __main__ import starter_list",
#         number=1000,
#     ),
# )
# # => 2.4483373747207224
# print(
#     "Generator Run 1 Time",
#     timeit.timeit(
#         "(el for el in starter_list if el%2==0)",
#         "from __main__ import starter_list",
#         number=1,
#     ),
# )
# # => 9.041279554367065e-06
# print(
#     "Generator Run 1000 Time",
#     timeit.timeit(
#         "(el for el in starter_list if el%2==0)",
#         "from __main__ import starter_list",
#         number=1000,
#     ),
# )
# # => 0.00024854158982634544
