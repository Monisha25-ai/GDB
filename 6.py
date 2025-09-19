#class, object , instance ,attribute, method
class car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
    def start(self):#this is a method
        print(f"The {self.color} {self.model} has started")
        #this method can be called with object of car class

    def stop(self):
        print(f"The {self.color} {self.model} has stopped")

    # we can use conditions in methods as well
    def accelerate(self, speed):
        if speed > 100:
            print("Speed cannot be more than 100")
        else:
            print(f"The {self.color} {self.model} is accelerating to {speed} km/h")


class electric_car(car):
    #for initializing the attributes in the constructor we can use conditions
    def __init__(self, color, model, year):
        if year < 2000 or year > 2022:
            print("Invalid year")
        else:
            self.color = color
            self.model = model
            self.year = year

    def fill_battery(self, capacity):
        print(f"The {self.color} {self.model} battery is filled to {capacity}%")

    def charge(self):
        print(f"The {self.color} {self.model} is charging")

    #child class
    def start(self):
        print(f"The {self.color} {self.model} electric car has started")

    #super() is used to call the parent class method

    def stop(self):
        super().stop()
        print("The electric car has stopped")



#creating object of car class
my_car = car("red", "Toyota", 2021)
my_car.start()
my_car.accelerate(60)
my_car.stop()

#creating object of electric_car class
my_electric_car = electric_car("blue", "Tesla", 2020)
my_electric_car.start()
my_electric_car.accelerate(80)
my_electric_car.fill_battery(70)
my_electric_car.charge()
my_electric_car.stop()
    
class Restaurant:
    def __init__(self, flavors):
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor, end=" ,")

class IceCreamStand(Restaurant):  # inherit from Restaurant
    def __init__(self, flavors):
        super().__init__(flavors)  # call parent initializer

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor, end=" ,")

icecream_stand = IceCreamStand(["vanilla", "chocolate", "strawberry"])
icecream_stand.display_flavors()

class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} makes a sound")

    def get_info(self):
        return f"{self.name} is a {self.species}"
    
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print(f"{super().make_sound} + ' and barks'")#mistake here is 

    def fetch(self):
        print(f"{self.name} the {self.species} is fetching")

cow = Animal("Cow", "Bovine")
cow.make_sound()
cow.get_info()

dog = Dog("Buddy", "Dog", "Labrador")
dog.make_sound()
dog.get_info()
dog.fetch()

name = "  vikas S  "
print(name.strip()) #remove spaces from both ends