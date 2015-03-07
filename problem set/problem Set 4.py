### WORD SCORES

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    result = 0
    for letter in word:
        result += SCRABBLE_LETTER_VALUES[letter]

    result *= len(word)

    if (len(word) == n):
        result += 50
        
    return result

	
	
	
### DEALING WITH HANDS

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy() 

    for letter in word:
        handCopy[letter] -= 1

    return handCopy

	
	
### VALID WORDS


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    return word in wordList and all(hand.get(a, 0) >= b for a, b in getFrequencyDict(word).items())

	
### HAND LENGTH

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    return sum(x for x in hand.values())

	
	
### PLAYING HANDS 

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)

    totalScore = 0
    output = "Run out of letters."
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == '.':
            output = "Goodbye!"
            break
        else:
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.")
            else:
                score = getWordScore(word, n)
                totalScore += score
                print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore))
                hand = updateHand(hand, word)
    print('{0:s} Total score: {1:d} points.'.format(output, totalScore))
 

### PLAYING A GAME

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    hand = False
    while True:
        user = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").lower()
        if user not in 'nre':
            print("Invalid command.")
        else:
            if user == 'r' and not hand:
                print("You have not played a hand yet. Please play a new hand first!")
            elif user == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand.copy(), wordList, HAND_SIZE)
            elif user == 'r' and hand:
                playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                break
            print("")

			

### COMPUTER CHOOSES A WORD

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    bestscore=0
    score=0
    bestword=None
    
    for words in wordList:
         if isValidWord(words, hand, wordList):
            score=getWordScore(words,sum(hand.values()))
            if score>bestscore:
                bestscore = score
                bestword = words
                
            
    return bestword

	
	
### COMPUTER PLAYING A HAND

def compChooseWord(hand, wordList, n):
    bestscore=0
    score=0
    bestword=None
    
    for words in wordList:
         if isValidWord(words, hand, wordList):
            score=getWordScore(words,sum(hand.values()))
            if score>bestscore:
                bestscore = score
                bestword = words
                
            
    return bestword




def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... 
    totalScore = 0
    
    while calculateHandlen(hand) > 0:
    
        print "Current Hand:",
        displayHand(hand)
        
        word = compChooseWord(hand, wordList, n)
        #print "Computer entered:", word
        
        if word == None:
            break;
        else:
            points = getWordScore(word, n)
            totalScore += points
            print "\""+word+"\" earned", points, "points. Total:", totalScore, "points"
            
            hand = updateHand(hand, word)
                
    print "Total score:", totalScore, "points."

	
	
### YOU AND YOUR COMPUTER

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
    
    def displayHand2(hand):
      displayed = ''
      for letter in hand.keys():
            for j in range(hand[letter]):
                 displayed += letter + ' '
      return displayed
    hand = False
    while True:
      ans = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
      if ans == "n":
        hand = dealHand(HAND_SIZE)

        tester1 = True
        while tester1:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
            tester1 = False
          elif ans2 == "c":
            compPlayHand(hand, wordList, HAND_SIZE)
            tester1 = False
          else:
            print "Invalid command."
      elif ans == "r":
        if hand:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
          elif ans2 == "c":

            compPlayHand(hand, wordList, HAND_SIZE)
          else:
            print "Invalid command."
        else:
          print "You have not played a hand yet. Please play a new hand first!"
      elif ans == "e":
        break
      else:
        print "Invalid command."

    
