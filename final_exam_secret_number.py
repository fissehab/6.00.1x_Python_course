"""
Answer the following question without running the code. The procedure isMyNumber is used to hide a secret number (integer). It takes an integer x as a parameter and compares it to the secret number. It returns:

    -1 if the parameter x is less than the secret number

    0 if the parameter x is correct

    1 if the parameter x is greater than the secret number

The following procedure, jumpAndBackPedal, attempts to guess a secret number. The only way it can interact with the secret number is through the isMyNumber procedure explained above.
"""

def isMyNumber(x):
    
    secret_number =199;
    if x ==secret_number:
        return 0
    if x > secret_number:
        return 1
    else:
        return -1
        
        
        


def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    
    while True:
     if isMyNumber(guess) == 0:
        break
     else:
      if isMyNumber(guess) == 1:
         guess=guess-1
      if isMyNumber(guess) == -1:
         guess=guess+1
    return guess
