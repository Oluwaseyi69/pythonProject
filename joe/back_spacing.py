def backspace(s):
    # global index
    # s = ""
    # t = ""
    # global new_s, new_t
    global new_s
    for index in s:
        if index == "#":
            new_s = s.replace("").replace("")
        print(new_s)


print(backspace("db#c"))
