from ps4a import *

handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word ='quail'


hand1=handOrig.copy()
handCopy=[]
handCopy=displayHand(hand1)

word_letters=list(word)
candidate =True

for letter in word_letters:
     
         handCopy.remove(letter)