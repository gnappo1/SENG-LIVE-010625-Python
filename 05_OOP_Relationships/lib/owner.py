class Owner:
    all_ = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all_.append(self)

    def pets(self): # one owner has many pets
        # go through all of the pets
        # filter by the owner being myself
        return [pet for pet in Pet.all_ if pet.owner == self]

from lib.pet import Pet
