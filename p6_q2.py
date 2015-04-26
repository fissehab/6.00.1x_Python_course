def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string 
    alphabet_lower=list(string.ascii_lowercase)  
    alphabet_upper=list(string.ascii_uppercase)
    dic={}  
    for i in range(0,len(alphabet_upper)):  
        dic[alphabet_lower[i]]=alphabet_lower[(i+shift)%len(alphabet_lower)]
        dic[alphabet_upper[i]]=alphabet_upper[(i+shift)%len(alphabet_upper)]
    return dic
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    dic=coder
    ciphertext=""  
    for i in text:  
        if i in dic:  
            i=dic[i]  
        ciphertext+=i  
  
    return ciphertext 
    
def applyShift(text, shift):   
      return applyCoder(text,buildCoder(shift))