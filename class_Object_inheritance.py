# Animal Kingdom!


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    def __init__(self, name, age,species):
        super().__init__(name, age)
        self.species = species
        
    def __str__(self):
        return (f"{self.name} is {self.age} years old & it is {self.species}")
    
    def make_sound(self):
        print("Tweet")


dog = Dog("Bulldog", 8, "no")
cat = Cat("Tom",5,"White")
bird = Bird("Moyna",1,"Black")
dog.make_sound()
print(f"{dog.name} is {dog.age} years old & it has {dog.breed} breed")

print(bird)