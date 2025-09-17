class Cat:
    def __init__(self, name, age,color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.",'i am',self.color)

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.","i am",self.color)

    def make_sound(self):
        print("Bark")


kitty= Cat("toby",2,"blue")
doggy= Dog("Tony",14,"red")

for animal in (kitty,doggy):
    animal.make_sound()
    animal.info()

