# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,word_list):
        return [w for w in  word_list if self.compare_words(w)]

    def compare_words(self,one_word):
        return sorted(self.word.lower()) == sorted (one_word.lower())