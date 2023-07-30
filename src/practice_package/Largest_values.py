largest = 0
largest_2 = 0

for x in range(10):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number
    # if number > largest_2:
    #     largest_2 = number
    if largest_2 < number < largest:
        largest_2 = number

print(f'The largest number is: {largest}')
print(f'The second largest number is: {largest_2}')
