class Student:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.__id = ID

    def get_id(self):
        return self.__id

    def info(self):
        print(self.name)
        print(self.age)


s3 = Student("Jeff", 6, 475)
s1 = Student("John", 14, 7563)
s2 = Student("Jack", 13, 563)

s2.info()
print(s2.get_id())


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def whole_name(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return "{}_{}@gmail.com".format(self.first, self.last)


x = Person("Krish", "Rastogi")

print(x.whole_name())
print(x.email())


class Dog:
    def __init__(self, weight, height, breed, name):
        self.weight = weight
        self.height = height
        self.breed = breed
        self.name = name

    def info(self):
        return "Hello my name is {}".format(self.name)

    def bark(self):
        return "The {} is barking".format(self.breed)

    def bmi(self):
        return int(self.weight / self.height)


Dog1 = Dog(30, 50, "golden retriever", "Terry the Legend")
Dog2 = Dog(900, 4, "poodle", "Fluffy the Amazing")

print(Dog1.info())
print(Dog1.bark())
print(Dog2.bmi())


class Bicycle:
    wheels = 2

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def about(self):
        return "This car is a {} {}".format(self.color, self.model)

    def ChangeColor(self, color):
        self.color = color


Bike1 = Bicycle("Red", "7X Extreme Fly")

Bike1.ChangeColor("Not Red")
print(Bike1.color)
