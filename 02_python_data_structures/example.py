class Vehicle:
    def __init__(self, color, brand, motorized): #! self is the newly created specific vehicle
        self.color = color
        self.brand = brand
        self.motorized = motorized
    
    def introduce(self):
        return f"I am a {self.brand} {self.color} car, and I {'am' if self.motorized else 'am not'} motorized"

class Car(Vehicle):
    pass

#! Instantiate objects outside of the class
porsche = Car("black", "Porsche", True)
fiat = Car("red", "Fiat", True)
carriage = Car("brown", None, False)

porsche.introduce()
import ipdb; ipdb.set_trace()
