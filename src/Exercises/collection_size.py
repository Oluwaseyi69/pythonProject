def collection_size(collection):
    count = 0
    for element in collection:
        count += 1
    return count


list1 = [1, 2, 3, 4], [3, 6, 4, 5], [5, 8, 7, ]
list2 = (1, 2, 3, 4), (1, 2, 4, 6), (5, 8, 7, ), 3, 6, 4, 5,
print(collection_size(list1))
print(collection_size(list2))

