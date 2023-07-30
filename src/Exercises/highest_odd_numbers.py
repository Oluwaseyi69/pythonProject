def highest_odd_number(array1):
    new_list = []
    for index in array:
        if index % 2 != 0:
            new_list.append(index)
    highest = new_list[0]
    for number in new_list[1:]:
        if number > highest:
            highest = number
    return highest


array = [15, 24, 2, 121, 33]

print(highest_odd_number(array))
