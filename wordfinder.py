"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        """read dict and return # of items"""
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse file into a list of words"""
        return [words.strip() for words in file]
    
    def random(self):
        """return a random word"""
        return random.choice(self.words)
    
    class SpecialWordFinder(WordFinder):
        def parse(self, file):
            return [words.strip() for words in file
                    if words.strip() and not words.startswith("#")]
