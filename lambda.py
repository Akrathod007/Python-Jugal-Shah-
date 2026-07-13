# def add(a, b):
#     return a + b


# print(add(10, 20))

# add2 = lambda a, b: a + b

# print(add2(10, 45))


# check = lambda n: "Even" if n % 2 == 0 else "Odd"

# print(check(10))
# print(check(11))


# check = lambda n: ("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

# print(check(10))
# print(check(-5))
# print(check(0))


# login = lambda user, pwd: (
#     "Admin Login"
#     if user == "admin" and pwd == "007"
#     else "User Login" if user == "user" and pwd == "xyz" else "Invalid Login"
# )

# print(login("admin", "123"))
# print(login("admin", "007"))
# print(login("user", "xyz"))


# def m(x, y, z):
#     if x > y:
#         if x > z:
#             return x
#         else:
#             return z
#     else:
#         if y > z:
#             return y
#         else:
#             return z


# m = lambda x, y, z: (x if x > z else z) if x > y else (y if y > z else z)
# print(m(10, 20, 30))
# print(m(40, 20, 30))
# print(m(10, 50, 30))


# Lambda with map :

# li = [1, 2, 3, 4, 5]

# x = list(map(lambda x: x * 2, li))
# print(x)

# y = list(map(lambda x: x * x, li))
# print(y)

# z = list(map(lambda n: n * n if n % 2 == 0 else n**3, li))
# print(z)


# def square(n):
#     return n * n


# y = list(map(square, li))
# print(y)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = list(filter(lambda x: x % 2 == 0, li))
print(x)


# Map Task :
"""
Create a list of numbers and use map() to find squares of all numbers.

Create a list of numbers and use map() to convert all numbers into strings.

Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.

Create a list of names and use map() to convert all names into uppercase.

Given a list of strings, use map() to find the length of each string.

Create a list of numbers and use map() to add 10 to every element.

Given a list of words, use map() to reverse each word.

Create a list of prices and use map() to add 18% GST to every price.

Create a list of integers and use map() to check whether each number is even or odd.
"""
"""
Filter Task :

1. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

2. Filter Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

3. Filter Positive Numbers
numbers = [-5, 10, -2, 8, 0]

4. Filter Names Starting With A
names = ["Akshay", "Rahul", "Amit", "Karan"]

5. Filter Strings With Length More Than 5
words = ["apple", "banana", "kiwi", "mango"]

6. Filter Vowels From List
letters = ['a', 'b', 'e', 'f', 'i']

7. Filter Palindrome Words
words = ["madam", "python", "level", "code"]

8. Filter Uppercase Words
words = ["HELLO", "Python", "WORLD", "Code"]

9. Filter Alphabet Characters
data = ['A', '1', 'B', '9', 'C']

10. Filter Strings Containing Letter "a"
words = ["apple", "mango", "berry", "banana"]
"""


from functools import reduce

# li = [1, 2, 3, 4, 5, 6]

# s = reduce(lambda x, y: x + y, li)
# print(s)

# mini = reduce(lambda x, y: x if x < y else y, li)
# print(mini)

# maximum = reduce(lambda x, y: x if x > y else y, li)
# print(maximum)

# x = reduce(lambda x, y: x + y, li, 10)
# print(x)


# sum of suqare of even numbers

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(filter(lambda x: x % 2 == 0, li))

square_even_nums = list(map(lambda x: x * x, even_num))

total = reduce(lambda x, y: x + y, square_even_nums)

print(even_num)
print(square_even_nums)
print(total)


total = reduce(
    lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, li))
)

print(total)
