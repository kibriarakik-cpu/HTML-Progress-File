class Dog(Animal):

    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)  # Calls Animal's constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")
class Parrot(Animal):

    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    # The code gets cut off, but it will implement speak() similarly:
    # def speak(self):
    #     print(f"{self.name} repeats: {self.phrase}")
# --- CHILD CLASS 3 ---------------------------------------
class Lion(Animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: ROARRR!")


# --- CREATE OBJECTS & RUN THE SHOW -----------------------
dog    = Dog("Bruno", "Home",      "Labrador")
parrot = Parrot("Polly", "Jungle",   "Squawk")
lion   = Lion("Simba", "Savannah", "Pride Rock")

print("=== Animal Sound Show ===\n")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()