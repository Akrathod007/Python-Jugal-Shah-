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


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Raju", 30)

del p1.age

print(p1.name)
# print(p1.age) #Error


class Person:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property


p1 = Person("Hatori")
p2 = Person("Doremee")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name


p1 = Person("Ram")
p2 = Person("Shyam")

Person.lastname = "Pandey"

print(p1.lastname)
print(p2.lastname)
