def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

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