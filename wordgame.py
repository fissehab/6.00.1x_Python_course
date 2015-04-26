# Fisseha Berhane
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem set 4




#dictionary = raw_input('Please give the word list file name\n\t') # This waits for the word list file name with appropriate extention

#f = open(dictionary, "r")

f = open('sowpods.txt', "r")

print''
print 'Loading word list from file...'

word_list =[]
for line in f:
    line = line.strip()
    word_list.append(line)
f.close()

print str(len(word_list))+' words loaded.'
print('')

SCRABBLE_LETTER_VALUES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

option = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:\n\t')

if option=='e':
   print '\t Ok, see you next time'
   
elif option=='n' or option=='r':
   hand=raw_input('Current Hand: ')
   hand_letters = list(hand)
   word = raw_input('Enter word, or a "." to indicate that you are finished: ')
   
  
      
   if word!='.':
     word_letters=list(word)
   
     candidate =True

     for letter in word_letters:
       if letter not in hand_letters:
         candidate=False
         break   # No need to keep checking letters.
       else:
        hand_letters.remove(letter)

   if candidate==True:
      if word in word_list:
     # Get the Scrabble SCRABBLE_LETTER_VALUES for each legal word
         total = 0
         for letter in word:
           total=total+SCRABBLE_LETTER_VALUES[letter]
         if len(word)==7:

             total=total*len(word)+50                                   # 50 point bonus for using all letters).

         else:
             total=total*len(word)
         if len(word)==7:
           print  '"%s"'%word + ' earned '+ str(total) +' points. Total: '+ str(total)+' points'
           print 'Run out of letters. Total score:'+str(total)+' points. Nice Job!!'
           exit                                                              # no nead to go any further
         else:
          print  '"%s"'%word + ' earned '+ str(total) +' points. Total: '+ str(total)+' points'
          print 'Current Hand: '+''.join(hand_letters)
      else:
         print 'That is not a valid word. Please provide a legal word'
         print 'Current Hand: '+''.join(hand_letters)
   else:
         print 'please provde a word from the hand you have'
   
   while len(hand_letters)>=2: 
    word = raw_input('Enter word, or a "." to indicate that you are finished: ')   
    if word=='.':
       print 'Total score: '+str(total)+' points.'
       break
    elif word!='.':  
     hand_letters2=hand_letters[:]
     word_letters=list(word)
     for letter in word_letters:
       if letter not in hand_letters:
         candidate=False
         break   # No need to keep checking letters.
       else:
        hand_letters.remove(letter)

     if candidate==True:
      if word in word_list:
     # Get the Scrabble SCRABBLE_LETTER_VALUES for each legal word
         tot=0
         for letter in word:
           tot=tot+SCRABBLE_LETTER_VALUES[letter]

         tot=tot*len(word)
         total = total+tot
         print  '"%s"'%word + ' earned '+ str(tot) +' points. Total: '+ str(total)+' points'
         print 'Current Hand: '+''.join(hand_letters)

      else:
         print 'That is not a valid word. Please choose another word'
         print 'Current Hand: '+''.join(hand_letters2)

     else:
         print 'please provde a word from the hand you have'
