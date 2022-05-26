from collections import Counter


def green(letter, ii):
    return lambda word: word[ii] == letter


def yellow(letter, ii):
    return lambda word: letter in word and word[ii] != letter


def grey(letter, count):
    # Note that we can get grey if a letter is present in the
    # target word, but we entered it too many times in our guess.
    return lambda word: Counter(word)[letter] <= count


def match_criteria(criteria, word):
    for c in criteria:
        if not c(word):
            return False
    return True


class Wordle:
    def __init__(self, wordlist):
        f = open(wordlist, 'r')
        self.w = [word.strip().lower() for word in f.readlines()]
        self.known_letters = set()

    def try_word(self, guess, result):
        # guess: 5-letter word
        # result: 5-char string of ‘0’, ‘1’ or ‘2’
        # 0: corresponding letter in guess is absent
        # 1: corresponding letter in guess is present but in wrong place
        # 2: corresponding letter in guess is present and in right place
        # Filters word list according to guess and result.
        # Prints out the length of the filtered wordlist.

        criteria = []
        letter_counter = Counter()
        for ii, token in enumerate(result):
            letter = guess[ii]
            if token == '0':
                criteria.append(grey(letter, letter_counter[letter]))
            elif token == '1':
                letter_counter[letter] += 1
                criteria.append(yellow(letter, ii))
                self.known_letters.add(letter)
            elif token == '2':
                letter_counter[letter] += 1
                criteria.append(green(letter, ii))
                self.known_letters.add(letter)
            else:
                raise ValueError("Illegal token: " + token)

        self.w = list(filter(lambda w: match_criteria(criteria, w), self.w))
        print("Narrowed down to {0} matches".format(len(self.w)))
        print("Suggested next guess is {0}".format(self.next_guess()))

    def next_guess(self):
        # Find a word that has the fewest letters already known to be present,
        # and the fewest repeated letters.
        word_scores = [[[] for _ in range(6)] for _ in range(6)]
        for ww in self.w:
            wset = set(ww)
            ii = len(self.known_letters.intersection(wset))
            jj = len(wset)
            word_scores[ii][jj].append(ww)
        for ii in range(5):
            for jj in range(5, -1, -1):
                if len(word_scores[ii][jj]) != 0:
                    return word_scores[ii][jj][0:40]
        return self.w[0:40]

    def repeat_letter(self, letter, count):
        self.w = list(word for word in self.w if Counter(word)[letter] == count)
