# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Fish/classes/spring_2015/6001x/problemset6/words.txt"


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList
    
def findBestShift(text):
    import string 
    alphabet_lower=string.ascii_lowercase  
    alphabet_upper=string.ascii_uppercase
  
    for key in range(len(alphabet_upper)):

       translated = ''
       for symbol in text:

        if symbol in alphabet_upper:

            num = alphabet_upper.find(symbol)

            num = num - key
            
            if num < 0:

                num = num + len(alphabet_upper)

            translated = translated + alphabet_upper[num]
            
        elif symbol in alphabet_lower:

            num = alphabet_lower.find(symbol)

            num = num - key
            
            if num < 0:

                num = num + len(alphabet_lower)

            translated = translated + alphabet_lower[num]
        else:

         translated = translated + symbol

       print('Key #%s: %s' % (key, translated))