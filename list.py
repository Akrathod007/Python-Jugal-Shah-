"""
list -> Mutable + Ordered
tupel -> Immutable + Ordered
dictionary -> Mutable + Unordered
set -> Mutable + Unordered + Unique Values

"""

"""
li = [1, 2, 3, 4, 5]
print(li)
print(type(li))

l2 = [1, 3.14, "Hello", True]
print(l2)

l3 = [1, 2, 3, 4, 3, 4, 5, 6, 7, 5, 6, 7, 8]
print(l3)
print(l3[1])
print(l3[-3])
print(l3[2:8])
print(l3[:7])
print(l3[2:])
print(l3[:])
print(l3[-4:])
print(l3[-8:-4])
print(l3[-4:-8])
print(l3[::1])
print(l3[::2])
print(l3[2:7:3])
print(l3[::-1])
print(l3[::-2])
print(l3[-4:-8:-1])
print(l3[3:-3])

"""
"""
l1 = [1, 2, 3, 4, 5, 2, 3, 7, 8, 4, 5, 3]
print(l1)
l1.append(10)
print(l1)
l1.insert(2, 200)
print(l1)

elm = l1.pop()
print(elm)
print(l1)

elm = l1.pop(4)
print(elm)
print(l1)

l1.remove(2)
print(l1)

# l2 = []
# l2.pop()

# l3 = [1, 2, 3]
# l3.pop(5)

# l1.clear()
# print(l1)

l4 = [10, 20, 30, 40, 50]

print(l1 + l4)
# print(l1 + l4 + 10)

# l1.extend(10)
l1.extend(l4)
print(l1)

# l1.sort()
# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1)

print(l1.index(3))
print(l1.index(3, 4))
# print(l1.index(3, 6, 8))

print(l1.count(3))

print(sum(l1))
print(max(l1))
print(min(l1))
print(len(l1))

"""
# l4 = [1, 2, 3, "Hello"]
# l4 = [1, 2, 3, 1.2]
# l4 = [1, 2, 3, True]
# l4 = [1, 2, 3, False]
# print(l4)
# print(sum(l4))

# del l1
# print(l1)

# Shallow Copy
# l2 = l1
# print(l2)
# l2[1] = 2000
# print(l2)
# print(l1)

# Deep Copy

# l3 = l1.copy()
# print(l3)
# l3[2] = 2000
# print(l3)
# print(l1)

# l4 = l1[:]
# print(l4)
# l4[2] = 2000
# print(l4)
# print(l1)


# Index :

# for i in range(len(l1)):
#     print(i, "->", l1[i])

# direct value :
# for i in l1:
#     print(i)


# i = 0

# while i < len(l1):
#     print(l1[i])
#     i += 1

"""
no = int(input("Enter a elements do you want : "))

li = []

for i in range(1, no + 1):
    n = int(input("Enter a number : "))
    li.append(n)

print(li)

"""

"""
x = [1, 2, 3, 4, [6, 7, 8, 9], [10, 11, [12, 23, 34]]]
print(x)
print(x[3])
print(x[4][2])
print(x[4][:3])
# print(x[3][1:2])

# print(sum(x))
print(len(x))
print(x[5][2][1])

"""

# li = [1, 2, 3, 2, 4, 5]

# print(1 in li)
# print(11 in li)
# print(11 not in li)
# print(1 not in li)

# unique = []
# i not in unique


r = int(input("Enter a row : "))
c = int(input("Enter a column : "))
ol = []
"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""

for i in range(1, r + 1):
    il = []
    for j in range(1, c + 1):
        no = int(input("Enter a number : "))
        il.append(no)
        # [1,2,3]
    ol.append(il)

print(ol)

