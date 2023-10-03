def split_list(lst):
    new_index = []
    for index in range(3):
        sublist = lst[index::3]
        new_index.append(sublist)
    return new_index


sample_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
sample_output = split_list(sample_input)
print(sample_output)
