import sys

# Implement the Animal superclass here
# Hint: Copy your Tiger class from Problem 4 and modify it to be more general
class Animal(object):
    def __init__(self,name,favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
    def sleep(self):
        print(self.name + " sleeps for 8 hours")
    ...
    # Implement the eat function here
    def eat(self,food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
    ...


class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")


# Copy your Bear class here
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")
    
    def sleep(self):
        print("%s hibernates for 4 months" % self.name)


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "marshmallows")
    
    def sleep(self):
        print("%s sleeps in a cloud" % self.name)


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "leaves")
    
    def eat(self, food):
        Animal.eat(self, food)
        if food != self.favoriteFood:
            print("YUCK! %s spits out %s" % (self.name, food))


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "pollen")
    
    def eat(self, food):
        Animal.eat(self, food)
        if food != self.favoriteFood:
            print("YUCK! %s spits out %s" % (self.name, food))

def test():
    def getline():
        # Read a line from standard input and strip surrounding whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's species, name and food to eat
        species = getline()
        name = getline()
        food = getline()
        animal = None
        # Check what species the animal is
        if species == "tiger":
            # Create a Tiger object
            animal = Tiger(name)
        elif species == "bear":
            # Create a Bear object
            animal = Bear(name)
        elif species == "unicorn":
            # Create a Unicorn object
            animal = Unicorn(name)
        elif species == "giraffe":
            # Create a Giraffe object
            animal = Giraffe(name)
        elif species == "bee":
            # Create a Bee object
            animal = Bee(name)
        else:
            # Create an Animal object
            animal = Animal(name, "kibble")
        # Test the animal's eat and sleep methods
        animal.eat(food)
        animal.sleep()


if __name__ == "__main__":
    test()




