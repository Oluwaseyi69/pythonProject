def count_names_starting_with_s(new_names):
    names = {}
    for name in new_names:
        if name.capitalize().startswith("S"):
            names[name.capitalize()] = names.get(name.capitalize(), 0) + 1

    return names


name = ['Seyi', "Sandra", "Kevin", "Tomide", "sandra", "Esther", "Sunmibare", "Selina", "Selina", "Seychelles"]
answer = count_names_starting_with_s(name)
print(answer)
