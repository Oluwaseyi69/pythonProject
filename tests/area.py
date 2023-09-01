import math


def area(radius):
    if type(radius) is not int and type (radius) is not float:
        raise TypeError ("Invalid number")


    if radius < 0:
        raise ValueError("invalid number")

    return math.pi * radius * radius







# def value(number):
#
#     if type(number) is not int:
#         raise TypeError("invalid number")
#     return number


print("%.2f"%area(4))

def subtraction(number1, number2):
    answer = number1 - number2
    return answer

subtraction(15,10)