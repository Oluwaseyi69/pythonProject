numbers = [5,5,8,8,8, 3, 66, 66, 1, 2]
max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# m = 0
# for number in numbers:
#     if number % 2 != 0:
#         print(number)
#         m += number
# print("total: ", m)

unique = []
for x in numbers:
    if x not in unique:
        unique.append(x)

print(unique)

