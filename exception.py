# no = int(input("Enter a number : "))
# print(no)
# print("End")

# code

# try:
#     no = int(input("Enter a number : "))
#     print(no / 0)
#     print(no)
# except:
#     print("An error occured")

# print("End")


# try:
#     no = int(input("Enter a number : "))
#     print(10 / no)
# except ZeroDivisionError:
#     print("Division By Zero")
# except ValueError:
#     print("Enter valid integer")


# try:
#     no = int(input("Enter a number : "))
#     print(10 / no)
#     d = {"Name": "Ram"}
#     print(d["Age"])
# except (ZeroDivisionError, ValueError, KeyError):
#     print("Error")

# try:
#     x = 10 / 0

# except Exception as e:
#     try:
#         print(10 / 0)
#     except Exception as e:
#         print("Error:", e)

# try:
#     num = int(input("Enter Number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result =", result)


# try:
#     print(10 / 0)

# except:
#     print("Error")

# finally:
#     print("Always Executes")


# age = -5
age = 10

if age < 0:
    raise ValueError("Age is not negative")

print("age :", age)


# balance = 500
# withdraw = 1000

# if withdraw > balance:
#     raise Exception("Insufficient Balance")


# try:
#     age = int(input("Enter Age: "))

#     if age < 18:
#         raise ValueError("You are not eligible")

#     print("Eligible")

# except ValueError as e:
#     print("Error:", e)


class InvalidMarksError(Exception):
    pass


# marks = -10

# if marks < 0:
#     raise InvalidMarksError("Marks cannot be negative")


try:
    # marks = -10
    marks = 10
    if marks < 0:
        raise InvalidMarksError("Marks can't be negative")
    print("Marks :", marks)
except InvalidMarksError as e:
    print(e)


balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount
    print("Remaining Balance:", balance)

except Exception as e:
    print(e)


try:
    print("Outer Try")

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Except: Cannot divide by zero")

except:
    print("Outer Except")


try:
    print("Outer Try")

    try:
        num = int("abc")

    except ZeroDivisionError:
        print("Inner Except")

except ValueError:
    print("Outer Except: Invalid Number")


try:
    file = open("data.txt")

    try:
        data = int(file.read())
        print(data)

    except ValueError:
        print("File contains invalid data")

    finally:
        file.close()
        print("File Closed")

except FileNotFoundError:
    print("File Not Found")
