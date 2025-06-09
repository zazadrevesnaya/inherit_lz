class Animal():
    def __init__(self,name, age, species):
        self.name = name
        self.age = age 
        self.species = species
    
    def make_sound(self):
        if self.species == "snake":
            print(f"{self.name}, {self.age} years old ({self.species}), makes a hissing sound.")
        elif self.species == "cat":
            print(f"{self.name}, {self.age} years old ({self.species}), makes a meowing sound.")
        elif self.species == "dog":
            print(f"{self.name}, {self.age} years old, ({self.species}) makes a barking sound,has ({self.breed}) breed, gurd status: ({self.guard_status})")
        elif self.species != ["snake" or "cat" or "dog"]:
            print("I don't have this animal in the database.")
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")
    def __del__(self):
        print(f"{self.name} удалён из памяти.")

class Dog(Animal):
    def __init__(self, name, age, species, breed,guard_status):
        super().__init__(name, age, species="dog")
        self.breed = breed
        self.guard_status = guard_status
    def __del__(self):
        print(f"{self.name} собака удалена из памяти.")

animals_list = [
    Animal("alena", 23 , "snake"),
    Animal("mila", 7 , "cat"),
    Dog("gavrik", 5 , "dog","retriever","guarding"),
    Dog("meloch", 2 , "dog","bigl","sleeping"),
    Dog("sosiska", 2 , "dog","hound","chilling")
]
