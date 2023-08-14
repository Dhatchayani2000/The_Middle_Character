class MiddleCharacter:

    def __init__(self, word):
        self.word = word

    def get_middle(self):
        length = len(self.word)
        middle_index = length // 2
        if length % 2 == 1:
            return self.word[middle_index]

        else:
            return self.word[middle_index - 1: middle_index + 1]

given_word = input("Enter a word: ")
middle_char = MiddleCharacter(given_word)
middle = middle_char.get_middle()
print("Middle character(s):", middle)
