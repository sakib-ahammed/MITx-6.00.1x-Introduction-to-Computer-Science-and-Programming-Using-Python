### RADIATION EXPOSURE

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
	radiation = 0
    count = start
    while count < stop:
        radiation += step * f(count)
        count += step
    return radiation
	
	
	
### HANGMAN PART 1: IS THE WORD GUESSED?

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

	
### PRINTING OUT THE USER'S GUESS

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += '_ '
    return string

	
### PRINTING OUT ALL AVAILABLE LETTERS

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    notGuessed = []
    for i in range(26):
        notGuessed += chr(i + ord('a'))
    for j in lettersGuessed:
        notGuessed.remove(j)
    string = ''
    for k in notGuessed:
        string += k
    return string


### HANGMAN PART 2: THE GAME

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long")
    print("-----------")
    lettersGuessed = []
    guesses = 8
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print("You have " + str(guesses) +" guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        while True:
            guessLetter = raw_input("Please guess a letter: ").lower()
            if guessLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                print("You have " + str(guesses) + " guesses left")
                print("Available Letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessLetter
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("Congratulations, you won!")
            break
        elif guessLetter in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            guesses -= 1
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


    
