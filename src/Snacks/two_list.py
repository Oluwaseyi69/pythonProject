
def two_list(first_list, second_list) -> tuple:

    new_list = [x for x in first_list if x in second_list]
    # new_list = [for x in first_list and second_list if x

    return tuple(set(new_list))


if __name__ == '__main__':
    list1 = [20, 40, 60, 75, 85, 20, 40]
    list2 = [42, 40, 85, 20, 68, 88, 95]

    print(two_list(list1, list2))
