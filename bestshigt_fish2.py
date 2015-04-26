# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Fish/classes/spring_2015/6001x/problemset6/words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open("C:/Fish/classes/spring_2015/6001x/problemset6/words.txt", 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList
    
def isWord(wordList, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    return random.choice(wordList)
def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    return open("story.txt", "r").read()

def buildCoder(shift):

    alphabet_lower=list(string.ascii_lowercase)  
    alphabet_upper=list(string.ascii_uppercase)
    dic={}  
    for i in range(0,len(alphabet_upper)):  
        dic[alphabet_lower[i]]=alphabet_lower[(i+shift)%len(alphabet_lower)]
        dic[alphabet_upper[i]]=alphabet_upper[(i+shift)%len(alphabet_upper)]
    return dic
def applyCoder(text, coder):
    
    dic=coder
    ciphertext=""  
    for i in text:  
        if i in dic:  
            i=dic[i]  
        ciphertext+=i  
  
    return ciphertext 
def applyShift(text, shift):

    return applyCoder(text,buildCoder(shift))


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    no_words =0
    best_Shift =0
    tmp_Shift  =0
    
    while tmp_Shift < 26:
      decodedMessage = applyShift(text,tmp_Shift)
      words = decodedMessage.split(" ")
      counter = 0
      for w in words:
       if isWord(wordList,w)==True:
          counter +=1
      if counter > no_words:
         no_words = counter
         best_Shift = tmp_Shift
      tmp_Shift += 1
    return best_Shift