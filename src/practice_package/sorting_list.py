number = [8, 2, 5, 6, 1, 3, 9, 4, 7]


# new_number = number.append(number)
# new_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for row in range(len(number)):
#     for row_ in range(len(number)):
#         if number[row] < number[row_]:
#             number[row], number[row_] = number[row_], number[row]
#
# print(number)


def even_number(number):
    new_number = []
    for rowe in number:
        if rowe % 2 == 0:
            new_number.append(rowe)
    return new_number


# result = [rowe for rowe in number if rowe % 2 == 0]
# print(result)

print(even_number(number))
