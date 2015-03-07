### PROBLEM 1: ENCRYPTION (BUILDCODER)  

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dd = { string.ascii_uppercase[i]: string.ascii_uppercase[(i+shift)%26]   for i in range(len(string.ascii_uppercase))}
    DDD = { string.ascii_lowercase[i]: string.ascii_lowercase[(i+shift)%26]   for i in range(len(string.ascii_lowercase))}
    ### TODO 
    dd.update(DDD)
    return dd
	
	
### PROBLEM 1: ENCRYPTION (APPLYCODER)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO]
    result = ''
    for i in text:
        if coder.get(i) != None:
            result += coder.get(i)
        else:
            result += i
    return result


### PROBLEM 1: ENCRYPTION (APPLYSHIFT)  

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    dd = { string.ascii_uppercase[i]: string.ascii_uppercase[(i+shift)%26]   for i in range(len(string.ascii_uppercase))}
    DDD = { string.ascii_lowercase[i]: string.ascii_lowercase[(i+shift)%26]   for i in range(len(string.ascii_lowercase))}
    dd.update(DDD)
    result = ''
    for i in text:
        if dd.get(i) != None:
            result += dd.get(i)
        else:
            result += i
    return result

	
### PROBLEM 2: DECRYPTION (FINDBESTSHIFT)

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    # Set the maximum number of real words found to 0.
    maxRealWords = 0

    # Set the best shift to 0.
    bestShift = 0

    # For each possible shift from 0 to 26:
    for shift in range(0,26):

	   # Shift the entire text by this shift.
       shiftedText = applyShift(text, shift)

	   # Split the text up into a list of the individual words.
       individualWords = shiftedText.split()

       # Count the number of valid words in this list.
       validWords = 0
       for word in individualWords:
           if isWord(wordList, word):
               validWords = validWords + 1

	   # If this number of valid words is more than the largest number of
	   # real words found, then:
       if validWords > maxRealWords:

           # Record the number of valid words.
           maxRealWords = validWords

	   # Set the best shift to the current shift.
           bestShift = shift

	   # Increment the current possible shift by 1. Repeat the loop
	   # starting at line 3.

    # Return the best shift.
    return bestShift

	
### PROBLEM 2: DECRYPTION (DECRYPTSTORY)  

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    wordList = loadWords()
    text = getStoryString()
    shift = findBestShift(wordList, text)
    return applyShift(text, shift)
