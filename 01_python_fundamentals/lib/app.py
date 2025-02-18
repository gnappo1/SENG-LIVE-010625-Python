#!/usr/bin/env python3

# 📚 Review With Students:
# Python environment set up
# Python debugging tools
# Python datatypes

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb
# ipdb.set_trace()

# TODO Data Types
# 0. Style Guide (https://peps.python.org/pep-0008/)
# a. Numeric: int, float, complex
# b. Sequence: tuple, list, range, str
# c. Boolean: bool (True, False)
# d. NoneType: None
# e. Mapping: dict, frozendict
# f. Sets: set, frozenset

# TODO Truthiness and Falseness
# Falsey: None, [], {}, set(), "", (), 0, 0.0, 0+0j

# 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# Note => Feel free to set your own values for "pet_mood" to view various outputs.
# TODO Naming Conventions
pet_mood = "Hungry!"
pet_name = "Rose"

# TODO conditional Statement
# ? Check out match/case statements in python 3.10
# if (pet_mood == "Hungry!"):
#     print(f"Feed {pet_name}!")
# elif pet_mood == "test":
#     print(f"Cuddle {pet_name}!")
# else:
#     print("Run!")

# TODO convert into ternary expression
# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."
# condition ? what do to if valid : what to do if invalid (JS)
# what do to if CONDITION else what to do if invalid (Python)
# print(f"Feed {pet_name}!") if pet_mood == "Hungry!" else print("Run!")


# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"
def say_hello():
    return "Hello, world!"

# print(say_hello())

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"
def pet_greeting(pet_name="Matteo"):
    return f"{pet_name} says hello!"
# print(pet_greeting("Fido"))

def introduce(first, second, *args, **kwargs):
    # args will be a tuple of all the required POSITIONAL args
    # kwargs will be a dict of all the required keyword args
    return f'Hello my name is {kwargs["name"]}, I am {kwargs["age"]} yo, and I am {kwargs["height"]} feet tall'

print(introduce(True, "hello", {}, age=33, name="Matteo", height=6.1))
# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."

# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"
def pet_birthday(age):
    # if type(age) != int:
    #     return "Age must be a int"
    try:
        return f"Happy Birthday! Your pet is now {age+1}."
    except Exception:
        return "Age must be a int"

print(pet_birthday("ooops"))

# Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()
