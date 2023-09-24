def palindrome():
    word = input("Enter a word: ").strip()
    if is_palindrome(word.casefold()):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")


def is_palindrome(word):
    low = 0
    high = len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False

        low += 1
        high -= 1

    return True


palindrome()
