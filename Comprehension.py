# s = []

# for i in range(1, 11):
#     s.append(i * i)

# print(s)

# s2 = [i * i for i in range(1, 11)]
# print(s2)


# e = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         e.append(i)

# print(e)


# e2 = [i for i in range(1, 21) if i % 2 == 0]
# print(e2)


# eo = []
li = [34, 56, 77, 89, 76, 45, 34, 22, 34, 33]

# for i in range(1, 11):
#     if i % 2 == 0:
#         eo.append("Even")
#     else:
#         eo.append("Odd")
# for i in li:
#     if i % 2 == 0:
#         eo.append("Even")
#     else:
#         eo.append("Odd")

# print(eo)


# eo = ["Even" if i % 2 == 0 else "Odd" for i in li]
# print(eo)


marks = [78, 99, 88, 67, 56, 72, 45, 34, 70, 23, 55]

# g = []

# for i in marks:
#     if i >= 90:
#         g.append("A")
#     elif i >= 80:
#         g.append("B")
#     elif i >= 70:
#         g.append("C")
#     elif i >= 60:
#         g.append("D")
#     elif i >= 50:
#         g.append("E")
#     else:
#         g.append("F")

# print(g)

# g = [
#     (
#         "A"
#         if i >= 90
#         else (
#             "B"
#             if i >= 80
#             else "C" if i >= 70 else "D" if i >= 60 else "E" if i >= 50 else "F"
#         )
#     )
#     for i in marks
# ]
# print(g)


# t = {i * i for i in range(1, 11)}
# print(t)

# s = {i * i for i in range(1, 11) if i % 2 == 0}
# print(s)

# d = {i: i * i for i in range(1, 11)}
# print(d)

# d2 = {i: i * i for i in range(1, 11) if i % 2 == 0}
# print(d2)

# d3 = {i: (i * i if i % 2 == 0 else i**3) for i in range(1, 11)}
# print(d3)

# keys = ["Name", "Age", "City"]
# values = ["Raj", 21, "Ahm"]

# d = {keys[i]: values[i] for i in range(len(keys))}
# print(d)


# no = int(input("Enter a list length : "))
# li = []

# for i in range(1, no + 1):
#     # n = int(input("Enter a number : "))
#     li.append(int(input("Enter a number : ")))
# print(li)

# l2 = [int(input("Enter a number : ")) for i in range(1, no + 1)]
# print(l2)


r = int(input("Enter a row : "))
c = int(input("Enter a column : "))
ol = []
for i in range(1, r + 1):
    il = []
    for j in range(1, c + 1):
        no = int(input("Enter a number : "))
        il.append(no)
        # [1,2,3]
    ol.append(il)

print(ol)


x = [
    [int(input("Enter a number : ")) for j in range(1, c + 1)] for i in range(1, r + 1)
]

print(x)
