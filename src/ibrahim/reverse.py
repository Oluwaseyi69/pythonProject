# def reversal(name) -> str:
#     new_name = ""
#     for index in name[len(name):: - 1]:
#         new_name += index
#     return new_name
#
#
# name = "Seyi"
# print(reversal(name))
#
#
# def reverse(string):
#     return string[:: -1]
#
#
# name = "Hello"
# print(reversal(name))




# number = 1

# for _ in range(1, 10):
#     for _ in range (1, _ + 1):
#         print("*" ,end= "")
#         # print()


for y in range(10):
    for _ in range(y):
        print("*", end="")
    for x in range(10 - y):
        # print("", end="")
        print()