nums = [False, False, True, False]
print(any(nums))

nums = [0, 0, 0, 5]
print(any(nums))

marks = [25, 30, 35, 80]
result = any(mark >= 40 for mark in marks)
print(result)

marks = [25, 30, 35, 80]
result = any(mark >= 90 for mark in marks)
print(result)

print("------------------------------------------------------------------------")
nums = [True, True, True]
print(all(nums))
nums = [True, False, True]
print(all(nums))
nums = [10, 20, 30]
print(all(nums))

marks = [50, 60, 70, 80]
result = all(mark >= 40 for mark in marks)
print(result)

marks = [50, 60, 20, 80]
print(all(mark >= 40 for mark in marks))

print("-------------------------------------------------------------------")

nums = [50, 10, 30, 20]
print(sorted(nums))
nums = [50, 10, 30, 20]
print(sorted(nums, reverse=True))
names = ["Raj", "Amit", "Kiran"]
print(sorted(names))
data = (5, 2, 8, 1)
print(sorted(data))

names = ["Python", "C", "Java", "JavaScript"]
print(sorted(names, key=len))

words = ["cat", "apple", "dog", "banana"]
print(sorted(words, key=lambda x: x[-1]))

nums = [-10, 5, -2, 8]
print(sorted(nums))
print(sorted(nums, key=abs))

student = {"name": "Raj", "age": 20, "city": "Ahmedabad"}

print(sorted(student))

people = [
    {"name": "Raj", "age": 25},
    {"name": "Amit", "age": 20},
    {"name": "Kiran", "age": 30},
]

result = sorted(people, key=lambda x: x["age"])
print(result)

students = [("Raj", 80), ("Amit", 60), ("Kiran", 90)]

print(sorted(students, key=lambda x: x[1]))
