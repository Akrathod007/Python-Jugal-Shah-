# s = {1, 2, 3, 4}
# print(s)
# print(type(s))

# l1 = [1, 2, 3, 2, 3]
# print(l1)

# s2 = set(l1)
# print(s2)

# s3 = set((1, 2, 2, 3, 4, 3, 2))
# print(s3)

# s4 = {}
# print(s4)
# print(type(s4))

# s5 = set()
# print(s5)
# print(type(s5))

# print(s3[0]) -> Error

# s6 = {[1, 2, 3]}
# s6 = {(1, 2, 3)}
# print(s6)

# s7 = {4, 6, 3, 1, 2, 7, 8, 9}
# print(s7)

# for i in s7:
#     print(i)


# s8 = {"apple", "mango", "kiwi", "banana", "watermelon"}
# print(s8)

# for i in s8:
#     print(i)

# s7 = {4, 6, 3, 1, 2, 7, 8, 9}
# print(s7)

# s7.add(200)
# s7.add(120)
# print(s7)

# s7.remove(2)
# s7.remove(22)
# s7.discard(2)
# s7.discard(22)
# elm = s7.pop()
# print(elm)
# print(s7)

# elm = s8.pop()
# print(elm)
# print(s8)

# s8.clear()
# print(s8)


a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # same
c = a.union(b)
print(c)
print(a)
print(a & b)  # {3}
print(a.intersection(b))  # same

print(a - b)  # {1, 2}
print(b.difference(a))  # same

print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))


a = {1, 2}
b = {1, 2, 3}

print(a <= b)  # True
print(a.issubset(b))  # True


print(b >= a)  # True
print(b.issuperset(a))  # True

x = {1, 2}
y = {3, 4}

print(x.isdisjoint(y))  # True

print("-----------------------------------------------------------------")
a = {1, 2}
b = {3, 4}

a.update(b)
print(a)  # {1, 2, 3, 4}

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)
print(a)  # {2, 3}

a = {1, 2, 3}
b = {2}

a.difference_update(b)
print(a)  # {1, 3}

a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)
print(a)  # {1, 2, 4}


fs = frozenset([1, 2, 3])
# fs.add(4)
# Error (immutable)
