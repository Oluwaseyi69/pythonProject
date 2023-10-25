def find_indices_with_highest_sum(x, y):
    if y <= 0:
        return "Invalid input for y"

    max_sum = -1
    result_indices = []

    for i in range(len(x) - y + 1):
        current_sum = sum(x[i:i + y])
        if current_sum > max_sum:
            max_sum = current_sum
            result_indices = list(range(i, i + y))

    return result_indices


x = [2, 4, 9, 3, 9, 1]
y = 2
output = find_indices_with_highest_sum(x, y)
print(output)
