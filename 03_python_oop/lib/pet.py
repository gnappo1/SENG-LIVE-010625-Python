# !/usr/bin/env python3
# Defines the location of the Python interpreter
# See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes

# 1. ✅ Create a Pet class
# Pet() -> create() -> init()
class Pet:
    def __init__(self, name, age, breed, species, temperament, owner): # init is for BIRTH and self is the newly created instance
        self.name = name
        self.age = age
        self.breed = breed
        self.species = species
        self.temperament = temperament
        self.owner = owner

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if not isinstance(new_name, str): # type(new_name) is not str
            raise TypeError("Name must be a string")
        elif len(new_name) < 1:
            raise ValueError("Name must be at least one letter")
        self._name = new_name
    
    name = property(get_name, set_name)

    def introduce(self):
        """returns the pet name and breed"""
        return f"Hello, my name is {self.name} and I am a {self.breed}"
    
    def __repr__(self):
        """returns official object representation"""
        
        return f"""
            Name: {self.name},
            Age: {self.age},
            Breed: {self.breed},
            Species: {self.species},
            Temperament: {self.temperament},
            Owner: {self.owner},
        """
    def __str__(self):
        """returns unofficial object representation, meaning print(object_name_here)"""
        
        return f"""
            Name: {self.name},
            Age: {self.age},
            Breed: {self.breed},
            Species: {self.species},
            Temperament: {self.temperament},
            Owner: {self.owner},
        """

# 2. ✅ Instantiate a few Pet instances

# Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__

# Add arguments to instances

# Attributes:
# name
# age
# breed
# temperament
# owner

# Use dot notation to access each Pet instance's attributes

# Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's
# attributes

# Review the "self" keyword

# Invoke "print_pet_details" on an instance

# Example Terminal Ouput:
# name: Rose
# age: 11
# breed: Domestic Longhair
# temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

# get_name => Retrieve Owner's name

# set_name => Set Owner's name

# Ensure that Owner's name is a String

# If not, issue warning of "Name must be a string"

# Use property() to compile get_name / set_name and invoke them
# whenever we access an Owner instance's name

# Object Properties => Attributes that are controlled by methods

fido = Pet(
    name="Fido",
    age=2,
    owner="Blair",
    breed="Doberman Pincher",
    species="dog",
    temperament="friendly",
)  # I just instantiated an object of the Pet class -> <__main__.Pet object at 0x102986090>
milo = Pet("Milo", 2, "Australian Shepard", "dog", "friendly", "Liam")  # <__main__.Pet object at 0x102986510>
fido.introduce()
milo.introduce()
import ipdb; ipdb.set_trace()
