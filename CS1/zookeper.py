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


# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")
    ...


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,"fish")
    def sleep(self):
        print(self.name+ " hibernates for 4 months")
    ...
# This code tests the Tiger and Bear classes and their eat and sleep methods
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
        else:
            # Create an Animal object
            animal = Animal(name, "kibble")
        # Test the animal's eat and sleep methods
        animal.eat(food)
        animal.sleep()


if __name__ == "__main__":
    test()

