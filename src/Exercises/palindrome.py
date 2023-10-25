# def word(string):
#     return string.casefold() == string[:: -1].casefold()
#
#
# print(word("Madam"))
#

def word(string):
    return string == string[:-1]


print(word("A better place"))
