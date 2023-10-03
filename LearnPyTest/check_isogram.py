class Isogram:
    def __init__(self, word):
        self.word = word

    def check_isogram(self, word) -> bool:
        return len(word) == len(set(word.lower() or word.isalpha()))




