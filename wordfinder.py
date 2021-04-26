"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ 
    >>> wf = WordFinder("words.txt")
    3 words read
    """

    def __init__(self, path):
        dictionary_file = open(src)

        self.words = self.parse(dictionary_file)

        print(f"{len(self.words)} words read")

    def parse(self, dictionary_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
   
    def parse(self, dictionary_file):
        return [w.strip() for w in dictionary_file
                if w.strip() and not w.startswith("#")]
    
