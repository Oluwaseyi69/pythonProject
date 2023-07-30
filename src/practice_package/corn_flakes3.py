picture = [
[ 0, 0, 0, 1, 0, 0, 0],
[ 0, 0, 1, 1, 1, 0, 0],
[ 0, 1, 1, 1, 1, 1, 0],
[ 1, 1, 1, 1, 1, 1, 1],
[ 0, 0, 0, 1, 0, 0, 0],
[ 0, 0, 0, 1, 0, 0, 0],
[ 0, 0, 0, 1, 0, 0, 0],
[ 0, 0, 0, 1, 0, 0, 0],
]

# for j in picture:
#      for p in j:
#          if p == 1:
#              print("*", end=" ")
#          if p == 0:
#              print(" ", end=" ")
#
# print(' '
# )


for j in picture:
      for p in j:
          if p == 1:
              print("*", end="")
          if p == 0:
              print(" ", end="")
      print()
#
# # for idx, v in enumerate("ace_clan"):
# for i,  v in enumerate("ace_clan"):
#     print(i, v)







# print
# print(f"""
#    *
#   ***
#  *****
# *******
#    *
#    *
#    *
#    *
#
# """
# )