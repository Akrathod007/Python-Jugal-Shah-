# t1 = ()
# print(t1)
# print(type(t1))

# t2 = (1, 2, 3, 4, 5)
# print(t2)

# t3 = (1, "Hello", 2.5, False)
# print(t3)

# li = [1, 2, 3, 4, 5]
# t4 = tuple(li)
# print(t4)
# print(type(t4))

# t5 = 1, 2, 3, 4, 5
# print(t5)

# print(t5[3])
# print(t5[-3])

# print(t5[2:4])

# # t5[2] = 200
# # print(t5)

# t6 = (10,)
# print(t6)
# print(type(t6))


# a = (1, 2, 3)
# b = (4, 5, 6)
# r = a + b
# print(r)

# print(a * 3)
# # print(a + 3)

# print(3 in a)
# print(33 in a)
# print(3 not in a)
# print(33 not in a)


# t7 = (1, 2, 3, 1, 2, 4, 5, 6, 3, 2, 8)

# print(len(t7))
# print(sum(t7))
# print(max(t7))
# print(min(t7))

# s = "Hello"
# t = tuple(s)
# print(t)

# print(t7.count(3))
# print(t7.index(2))
# print(t7.index(2, 3))
# print(t7.index(2, 5, 11))


# t = 1, "Ram", 98, 1, 2, 3, 4, 5
# print(t)

# roll, name, marks, *other = t
# print(roll)
# print(name)
# print(marks)
# print(other)


li = [5, 3, 2, 1, 4]

"""
li = 5 3 2 1 4

pass 1 :
    subpass1 : 3 5 2 1 4
    subpass2 : 3 2 5 1 4
    subpass3 : 3 2 1 5 4
    subpass4 : 3 2 1 4 5
    
pass2 : 
    subpass1 : 2 3 1 4 5
    subpass2 : 2 1 3 4 5
    subpass3 : 2 1 3 4 5
    
pass3 :
    subpass1 : 1 2 3 4 5
    subpass2 : 1 2 3 4 5

pass4 : 
    subpass1 : 1 2 3 4 5

"""
# c = 0
# for i in range(len(li)):
#     for j in range(len(li) - 1 - i):
#         if li[j] > li[j + 1]:
#             li[j], li[j + 1] = li[j + 1], li[j]
#         c += 1

# print(li)
# print("Count :", c)


"""
    li = 78 99 23 78 12
    
    max = li[0]
    smax = li[0]
    
    li[1]>max
    
    smax = max
    max = li[1]
    
"""


li = [34, 56, 78, 78, 45]
max = li[0]
s_max = li[0]

for i in li:
    if i > max:
        s_max = max
        max = i
    elif i > s_max and i != max:
        s_max = i

print("Max : ", max)
print("Second Max : ", s_max)
