# Errors and exceptions homework
# Problem 1:
def problem_1():
    for i in [2,3,'c',5]:
        try:
            x = i**2
            print(x)
        except TypeError:
            print("You fool! You can't square an integer")
            break
# Problem 2:
a = 5
b = 0
def problem_2():
    try:
        print(a/b)
    except ZeroDivisionError:
        print("No division by zero!!!")
# Problem 3:
def problem_3():
    while True:
        try:
            numz = int(input("Please enter a number to square: "))
        except TypeError:
            print("?")
            continue
        else:
            print("No error here")
            print(numz**2)
            break
        finally:
            print("hey wait a minute what am I doing here")
problem_3()