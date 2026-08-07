class Parrot:
    def __init__(self, name):
        self.name = name
        self.sing = self._sing

    def speak(self):
        return f"{self.name} says: Squawk!"
blue_parrot = Parrot("Blue")
print(blue_parrot.speak())
woo_parrot = Parrot("Woo")
print(woo_parrot.speak())
print("Blue is a{} ".format("blue.species of parrot"))
print("Woo is also a{} ".format("woo.species of parrot"))
print("{} is {} years old".format(blue_parrot.name, 5))
print("{} is {} years old".format(woo_parrot.name, 3))
def sing(self):
    return f"{self.name} sings a beautiful song!"
def sing(self, song):
    return f"{self.name} sings: {song}"
print(blue_parrot.sing("Happy Birthday"))
print(woo_parrot.sing("Twinkle Twinkle Little Star"))
print("{} dances gracefully.".format(blue_parrot.name))
print("{} dances gracefully.".format(woo_parrot.name))