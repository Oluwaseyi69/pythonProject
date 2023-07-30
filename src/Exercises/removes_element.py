def remove_element(number):
    list1 = []
    for element in number:
        if element not in list1:
            list1 += [element]
    return list1


listing = {1, 2, 2, 4, 4, 4, 5, 5}
print(remove_element(listing))
