class Bag:
    def __init__(self, color, capacity):
        self.color = color  # Bag color
        self.capacity = capacity  # Bag capacity in liters
    
    def open_bag(self):
        return f"The {self.color} bag is now open."
    
    def close_bag(self):
        return f"The {self.color} bag is now closed."


class Dog:
    def __init__(self, name, breed):
        self.name = name  # Dog's name
        self.breed = breed  # Dog's breed
    
    def bark(self):
        return f"{self.name} is barking!"
    
    def sit(self):
        return f"{self.name} is sitting."


class Cat:
    def __init__(self, name, color):
        self.name = name  # Cat's name
        self.color = color  # Cat's color
    
    def meow(self):
        return f"{self.name} is meowing!"
    
    def sleep(self):
        return f"{self.name} is sleeping."


class Cup:
    def __init__(self, material, size):
        self.material = material  # Cup material (e.g., plastic, glass)
        self.size = size  # Cup size (e.g., small, medium, large)
    
    def fill(self):
        return f"The {self.size} {self.material} cup is now filled with liquid."
    
    def empty(self):
        return f"The {self.size} {self.material} cup is now empty."


class Joel:
    def __init__(self, age, profession):
        self.age = age  # Joel's age
        self.profession = profession  # Joel's profession
    
    def introduce(self):
        return f"Hi, I'm Joel. I'm {self.age} years old and I work as a {self.profession}."
    
    def code(self):
        return f"Joel is coding!"
