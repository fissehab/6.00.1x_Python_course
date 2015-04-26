import string

WORDLIST_FILENAME = "C:/Fish/classes/spring_2015/6001x/problemset6/words.txt"

def findBestShift(wordList, text):
    
 """
 Finds a shift key that can decrypt the encoded text.
 text: string
 returns: 0 <= int < 26
 """

 noWords=0
 bestShift=0
 Shift=0
 while Shift<26:
  decodedMessage = applyShift(text,Shift)
  words = decodedMessage.split(" ")
  counter = 0
for w in words:
if isWord(wordList,w)==True:
counter +=1
if counter > noWords:
noWords = counter
bestShift = Shift
Shift += 1
return bestShift