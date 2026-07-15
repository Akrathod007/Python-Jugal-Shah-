# class Student:
#     name = "Raj"
#     age = 22

#     def display(self):
#         print(f"{self.name} and {self.age}")


# s1 = Student()

# print(s1.name)
# print(s1.age)
# s1.display()

# s2 = Student()

# s2.name = "Shyam"
# s2.age = 21
# s2.city = "Ahm"
# print(s2.city)
# s2.display()


# class Student:
#     # def __init__(self):
#     #     print("Hello")
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"{self.name} and {self.age}")


# s1 = Student("Ansh", 22)
# s1.display()
# s2 = Student("Ram", 24)
# s2.display()
# s3 = Student("Shyam", 23)
# s3.display()


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age


# p1 = Person("Ram")
# p2 = Person("Shyam", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country


# p1 = Person("Ram", 30, "Ahm", "India")

# print(p1.name)
# print(p1.age)
# p1.age = 26
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printname(self):
#         print(self.name)


# p1 = Person("Doremon")
# p2 = Person("Shinchan")

# p1.printname()
# p2.printname()


# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age

#     def greet(abc):
#         print("Hello, my name is " + abc.name)


# p1 = Person("Emil", 36)
# p1.greet()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")


# car1 = Car("BenZ", "Maybec", 2020)
# car1.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome")


# p1 = Person("Tilak")
# p1.welcome()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Raju", 30)

# del p1.age

# print(p1.name)
# # print(p1.age) #Error


# class Person:
#     species = "Human"  # Class property

#     def __init__(self, name):
#         self.name = name  # Instance property


# p1 = Person("Hatori")
# p2 = Person("Doremee")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)


# class Person:
#     lastname = ""

#     def __init__(self, name):
#         self.name = name


# p1 = Person("Ram")
# p2 = Person("Shyam")

# Person.lastname = "Pandey"

# print(p1.lastname)
# print(p2.lastname)


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def multiply(self, a, b):
#         return a * b


# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! You are now {self.age}")


# p1 = Person("Ram", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Shyam", 36)
# print(p1)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} ({self.age})"


# p1 = Person("Tilak", 36)
# print(p1)


# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Removed: {song}")

#     def show_songs(self):
#         print(f"Playlist '{self.name}':")
#         for song in self.songs:
#             print(f"- {song}")


# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()


# xyz = Playlist("My XYZ")
# xyz.add_song("ABC")
# xyz.add_song("PQR")
# xyz.show_songs()
# xyz.remove_song("ABC")
# xyz.show_songs()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello!")


# p1 = Person("Emil")

# del Person.greet

# p1.greet() #Error


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks  # private variable

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.__marks)


# s = Student("Ansh", 90)
# s.display()
# print(s.name)
# # print(s.__marks) #Error


# class Student:

#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, m):
#         if m < 0:
#             print("Wrong Marks")
#         else:
#             self.__marks = m

#     def get_marks(self):
#         return self.__marks


# s = Student()

# s.set_marks(95)
# # s.set_marks(-95)
# print("Marks:", s.get_marks())


# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print("Balance:", self.__balance)


# acc = BankAccount(1000)

# acc.deposit(500)
# acc.show_balance()


# Inheritance :


# Single Inheritance
class Animal:

    def eat(self):
        print("Animals eat food")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()


# Multiple Inheritance
class Father:
    def skill1(self):
        print("Driving")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    def skill3(self):
        print("Playing")


c = Child()
c.skill1()
c.skill2()
c.skill3()


# Multilevel Inheritance


class Grandfather:
    def house(self):
        print("Grandfather's house")


class Father(Grandfather):
    def car(self):
        print("Father's car")


class Son(Father):
    def bike(self):
        print("Son's bike")


s = Son()

s.house()
s.car()
s.bike()


# Hierarchical Inheritance


class Animal:
    def eat(self):
        print("Animals eat food")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.eat()
c.eat()


"""
        Vehical
        /     \
     NCar     SCar
      \      /
        ECar
"""

# Method Overriding in Inheritance : Sometimes a child class modifies the method of the parent class.


class Animal:

    def sound(self):
        print("Animals make sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()
d.sound()


# Using super() in Inheritance : super() is used to call parent class methods inside the child class.


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


s = Student("Ansh", 95)

print(s.name)
print(s.marks)
