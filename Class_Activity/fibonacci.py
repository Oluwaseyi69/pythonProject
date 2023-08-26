n =8

num1 = 0
num2 = 1
new_number = num2
count = 0

while count <= n:
    print(new_number, end=" ")
    count += 1
    num1, num2 = num2, new_number
    new_number = num1 + num2
# print()


# def Area(radius):
#     area = 3.143 * radius * radius
#     return area
#
# new_area = Area(2)
# print(new_area)