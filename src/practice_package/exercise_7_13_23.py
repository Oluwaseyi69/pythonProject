sum = 0
number = [10, 20, 30, 40, 50]

number = [10 + 20 + 30 + 40 + 50]
# number = (10 + 30 + 50)
for value in number:
    sum += value
    print(sum)

square = []
for value in range(len(number)):
    x = number[value] ** 2
    square = [x]
print(square)
#
# largest = square[0]
# smallest = square[0]
# for value in range(len(number)):
#     if square[value] < smallest:
#         smallest = square[value]
#     if square[value] > largest:
#         largest = square[value]
# print("The different is: ", largest - smallest)

    # print(number)

# # l1[number] = l1[item] ** 2
#
#     item[number] = item[number] + + 2
#     print(item)
