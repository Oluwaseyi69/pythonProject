def add(number):
    total = 0
    for digit in number:
        # if int(number) < 0:
        #     return number
        # if number > 0:
        new_number = int(digit)
        if new_number > 9:
            new_number -= 9
        total += new_number

    if total > 9:
        return add(str(total))
    else:
        return total


if __name__ == '__main__':
    numbers = "38"
    print(add(numbers))
