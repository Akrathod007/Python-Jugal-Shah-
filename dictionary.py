# user = {"name": "Ram", "age": 21, "city": "Ahm"}

# print(user)
# print(type(user))

# person = dict(name="Shyam", age="22")
# print(person)

# print(user["name"])
# print(user.get("age"))

# # print(user["state"])
# print(user.get("state"))

# del user["age"]
# print(user)

# elm = user.pop("age")
# elm = user.pop("state")
# elm = user.pop("state", "Not Found")
# print(elm)
# print(user)

# x = user.popitem()
# print(x)
# print(user)

# user.clear()
# print(user)


# d = {}
# print(d)


# for i in user:
#     print(i, "->", user[i])
#     # print(i, "->", user.get(i))

# for i in user.keys():
#     print(i, "->", user[i])

# for i in user.values():
#     print(i)


# for k, v in user.items():
#     print(k, "->", v)

# print(user.keys())
# print(user.values())
# print(user.items())


# user = {"name": "Ram", "age": 21, "city": "Ahm"}

# print(user)

# user["city"] = "Surat"
# user["state"] = "Guj"
# print(user)


# word = "mississippi"

# d = {}

# for w in word:
#     d[w] = d.get(w, 0) + 1

# print(d)


# d = {"a": 1, "b": 2, "c": 2, "d": 1, "e": 3}

# duplicate = []

# value = list(d.values())
# print(value)

# for i in value:
#     if value.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)

# print(duplicate)


# student = {"name": "Raju", "age": 21}
# print(student.get("name"))
# print(student.get("city", "Not Found"))

# student = {"name": "Raju", "age": 21}
# student.update({"age": 22, "city": "Surat"})
# print(student)


student = {"name": "Raju", "age": 21}
new_student = student.copy()
print(new_student)
# new_student["city"] = "Surat"
# print(new_student)
# print(student)

# keys = ["math", "science", "english"]
# marks = dict.fromkeys(keys, 0)
# print(marks)

# student = {"name": "Raju"}
# print(student.setdefault("age", 20))
# print(student)

print(len(student))


keys = ["Name", "Age", "City"]
values = ["Ram", 21, "Ahm"]

d = dict(zip(keys, values))
print(d)
