# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet:
    all = {}

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    #! Instantiation -> initialize an instance (object) out of a class
    #! Creation -> Persistence, the object data is INSERTED INTO the db table

    def __init__(self, name, species, breed, temperament, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Names must be at least one char long")
        else:
            self._name = new_name

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be of type string")
        elif not new_breed:
            raise ValueError("Breeds must be at least one char long")
        else:
            self._breed = new_breed

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    species TEXT,
                    breed TEXT,
                    temperament TEXT
                );
            """)
        except Exception as e:
            return e

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """DROP TABLE IF EXISTS pets;"""
            )
        except Exception as e:
            return e

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                        INSERT INTO pets (name, species, breed, temperament) VALUES (?, ?, ?, ?)
                    """, (self.name, self.species, self.breed, self.temperament),
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
        except Exception as e:
            return e

        #     CURSOR.execute(
        #         f"""
        #         INSERT INTO pets (name, species, breed, temperament) VALUES (?, ?, ?, ?)
        #     """,
        #         (self.name, self.species, self.breed, self.temperament),
        #     )
        #     CONN.commit()
        #     self.id = CURSOR.lastrowid
        # except Exception as e:
        #     CONN.rollback()
        #     return e

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament):
        new_pet = cls(name, species, breed, temperament) # instantiate an object
        new_pet.save() #persist the object
        return new_pet # expose the object to be reused

    # ✅ 6. Add "update" Instance Method to Update the db based on its Attributes
    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                        UPDATE pets SET name=?, species=?, breed=?, temperament=? WHERE id = ?
                    """,
                    (self.name, self.species, self.breed, self.temperament, self.id),
                )
                type(self).all[self.id] = self #! store in all the updated version of the object
        except Exception as e:
            return e
    # ✅ 7. Add "new_from_db" Class Method to Instantiate a new "pet" Instance from a row of pet Attributes From DB

    @classmethod
    def new_from_db(cls, row_of_data):
        try:
            return cls(
                row_of_data[1],
                row_of_data[2],
                row_of_data[3],
                row_of_data[4],
                row_of_data[0])
        except Exception as e:
            return e

    # ✅ 8. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        #!hey pets table gimme all of your rows
        #! for each ROW OF DATA (1, "Fido", "Dog", "Jackapoo", "Playful") INSTANTIATE AN OBJECT
        try:
            # with CONN: #! commit/rollback are ONLY NEEDED for non-retrieving operations (create, update, delete)
            CURSOR.execute(
                f"""
                    SELECT * FROM pets;
                """,
            )
            rows = CURSOR.fetchall()
            return [cls.new_from_db(row) for row in rows]
        except Exception as e:
            return e

    # ✅ 9. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name(cls, name_to_find_by):
        try:
            CURSOR.execute(
                """
                    SELECT * FROM pets
                    WHERE name = ?
                    LIMIT 1;
                """, (name_to_find_by,)
            )
            row_of_data = CURSOR.fetchone()
            return cls.new_from_db(row_of_data) if row_of_data else None
        except Exception as e:
            return e
# If No "pet" Found, return "None"

# ✅ 10. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

# If No "pet" Found, return "None"

# ✅ 11. Add "find_or_create_by" Class Method to:

#  Find and Retrieve "pet" Instance w/ All Attributes

# If No "pet" Found, Create New "pet" Instance w/ All Attributes

Pet.drop_table()
Pet.create_table()
princess = Pet("Princess", "Fish", "Clown Fish", "Playful")
princess.save()
fido = Pet.create("Fido", "Dog", "Jackapoo", "Playful")
fido.name = "Milo"
fido.update()
# Pet.get_all()
Pet.find_by_name("Milo")
import ipdb; ipdb.set_trace()
