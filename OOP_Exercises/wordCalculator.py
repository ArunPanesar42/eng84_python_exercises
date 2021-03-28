class Scrabble:

    def __init__(self):
        # set up a dictionary of letters and their values
        self.letters = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
                        'D': 2, 'G': 2,
                        'B': 3, 'C': 3, 'M': 3, 'P': 3,
                        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                        'K': 5,
                        'J': 8, 'X': 8,
                        'Q': 10, 'Z': 10}

    def calculate_score(self, word):
        word = word.upper()  # to make sure it matches the dictionary
        word_score = 0

        for letter in word:
            word_score += self.letters[letter]  # adds current letter value to the users Scrabble Score

        return word_score


user_score = Scrabble()

## user_word = input("Please enter your Word")

print(user_score.calculate_score("ocean"))
