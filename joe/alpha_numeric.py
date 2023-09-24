def new_number(number):
    largest = second_largest = float('-inf')

    for char in number:
        if char.isdigit():
            digit = int(char)
            if digit > largest:
                second_largest = largest
                largest = digit
            elif second_largest < digit < largest:
                second_largest = digit

    if second_largest != float('-inf'):
        return second_largest
    else:
        return -1


result = new_number("abc1234111")
print(result)
