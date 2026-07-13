# import math

# print(math.pi)
# print(math.e)
# print(math.pow(2, 5))
# print(math.pow(2, math.pow(2, 2)))

# import math as m

# print(m.pi)
# print(m.sqrt(25))
# print(m.cbrt(27))
# print(m.ceil(4.3))
# print(m.floor(4.3))
# print(m.ceil(-4.3))
# print(m.floor(-4.3))
# print(m.trunc(4.5))
# print(round(4.3))
# print(round(4.5))
# print(round(4.6))

# print(m.gcd(12, 18))
# # 12 -> 1,2,3,4,6,12
# # 18 -> 1,2,3,6,9,18
# print(m.lcm(12, 18))

# print(m.factorial(5))
# # %
# print(m.fabs(-2.5))
# print(m.fmod(4, 2))

# print(m.fmod(1.2, 0.5))

# print(m.log10(10))
# print(m.log2(10))
# print(m.log(10))

# print(m.inf)

# print(500000000000000000000000000000000000000000000000 > m.inf)


# from math import pow as p, sqrt

# print(pow(2, 4))
# print(p(2, 5))
# print(sqrt(25))

# from math import *

# print(cbrt(27))

import random as r

# from random import random
# from random import choice as ch,sample
# from random import *

# print(r.random())
# print(r.randint(1, 6))

# print(r.randrange(1, 6))
# print(r.randrange(1, 6, 2))
# print(r.randrange(1, 6, 3))


# fruits = ["Apple", "Banana", "Kiwi", "Mango"]
# print(r.choice(fruits))
# print(r.choices(fruits, k=3))
# print(r.sample(fruits, k=3))


# li = [1, 2, 3, 4, 5, 6, 7]
# r.shuffle(li)
# print(li)

# print(r.uniform(1.1, 2.2))


# Random Password Generator :
"""
1. Write a program to generate a 4-digit OTP.

2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 34
    match = 2
Check how many matches.

3. Write a program to generate a random HEX color code like #A3F4C1.

4. Write a program to guess the Number Game

randomNo = 1 to 25 (18)

while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
 


5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win


"""
# import string as s

# print(s.ascii_letters)
# print(s.ascii_lowercase)
# print(s.ascii_uppercase)
# print(s.digits)
# print(s.hexdigits)
# print(s.octdigits)
# print(s.punctuation)
# print(s.whitespace)

# Check digits in a string :
# Count alphabets in a string :
# Random Password Generator :


import datetime as dt

today = dt.date.today()
print(today)

t = dt.datetime.now()
print(t)

d = dt.date(2025, 1, 1)
print(d)

print(today.day)
print(today.month)
print(today.year)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

print(t.strftime("%d-%m-%Y"))
print(t.strftime("%d-%m-%y"))
print(t.strftime("%A %a %B %b"))

print(t.strftime("%H %p"))
print(t.strftime("%I %p"))
print(t.strftime("%H:%M:%S.%f"))
print(t.strftime("%j"))
print(t.strftime("%U"))
print(t.strftime("%W"))
print(t.strftime("%c"))
print(t.strftime("%x"))
print(t.strftime("%X"))

t = dt.datetime(2025, 12, 12, 15, 30, 20)
print(t)
print(t.strftime("%H %p"))
print(t.strftime("%I %p"))


today = dt.date.today()
new_date = today + dt.timedelta(days=5)

print(new_date)


d1 = dt.date(2026, 2, 8)
d2 = dt.date(2026, 2, 1)

diff = d1 - d2
print(diff.days)


time_now = dt.datetime.now().time()
print(time_now)


date_string = "08-02-2026"
date_obj = dt.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)
