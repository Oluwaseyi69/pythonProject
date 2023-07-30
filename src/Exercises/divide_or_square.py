# def divide_or_square(number):
#     if number % 5 == 0:
#         square_root = number ** 0.5
#         return square_root
#     else:
#         return number % 5 != 0
#
#
# print(f"{divide_or_square(100): .2f}")
#
#
#
# t1 = (1, 2, 3, [1, 2, 3], 3)
# x = t1[0] + t1[2]
# print(list(t1))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ([i ** 2 for i in list1])
answer = [i for i in result if i % 2 == 0]
print(result)
print(answer)
