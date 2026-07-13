# Types of user defined function :
# 1. No Return Type and No Arguments


# def sayHi():
#     print("Hello")


# sayHi()

# # 2. No Return Type and With Arguments


# def add(a, b):
#     print("Addition :", (a + b))


# add(4, 10)
# add(14, 20)
# add(45, 17)

# # 3. With Return Type and No Arguments


# def mul():
#     n1 = int(input("Enter a number 1 : "))
#     n2 = int(input("Enter a number 2 : "))
#     # print(n1 * n2)
#     return n1 * n2


# x = mul()
# print(x)

# print(mul())


# 4. With Return Type and With Arguments


# def swapCase(ch):
#     if ch >= "A" and ch <= "Z":
#         ch = chr(ord(ch) + 32)
#     elif ch >= "a" and ch <= "z":
#         ch = chr(ord(ch) - 32)

#     return ch


# y = swapCase("A")
# print(y)
# y = swapCase("q")
# print(y)
# y = swapCase("j")
# print(y)


# def add(a, b=30, c=30):
#     print(a + b + c)


# add(10, 20)
# add(20)
# add(10, 20, 40)


# def add(a, b, *args):
#     print(a)
#     print(b)
#     print(args)


# add(10, 20, 30, 40, 50, 60)


# def demo(a, b, **kargs):
#     print(a)
#     print(b)
#     print(kargs)


# demo("Hi", 10, name="Hello", age=21)


# def demo(a, *args, **kargs):
#     print(a)
#     print(args)
#     print(kargs)


# demo(10, 20, "Hi", "Bye", name="Ram", city="Ahm")


# def add(a, b):
#     print("a :", a)
#     print("b :", b)
#     print(a + b)


# add(10, 20)

# add(a=20, b=30)

# add(b=10, a=40)
"""
y = 1000
def sayHello():
    x = 10
    print(x)
    print(y)
    print("Hello")

sayHello()
# print(x)
print(y)


x = 10
def change():
    # x = 10
    global x
    x = x + 5  # Error
    print(x)

change()

x = 100
def demo():
    x = 50  # Local variable
    print(x)
demo()
print(x)

"""


def greet():
    print("Hello")


x = greet  # No ()
x()


def greet():
    print("Hello")


def call_func(func):
    func()


call_func(greet)


def outer():
    def inner():
        print("Inner function")

    return inner


# f = outer()
# f()

# f = outer
# print(f()())


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


ops = [add, sub]

print(ops[0](10, 5))
print(ops[1](10, 5))


def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()


def outer():
    x = 10

    def inner():
        # print(x)
        nonlocal x
        x = x + 10
        print(x)

    inner()


outer()
