def guessWord():
    # homework eliminate this as a function
    letter_guess = input("Guess a letter").lower()

    return letter_guess


def didUserWin(wordList):
    gCheck = []
    # homework generate gCheck by list comprehension
    for l,v in wordList:
        gCheck.append(v)

    # homework: use any() or all()
    if False in gCheck:
        return False
    else:
        return True

    '''   
    if False in wordList[:][1]:
        return False

    else:
        return True
    '''


def checkGuess(letter_guess, letterList):

    elcount = 0
    letter_found = False

    for l,v in letterList:
        if letter_guess == l:
            letter_found = True
            letterList[elcount] = (letter_guess, True)
        elcount += 1
    if letter_found:
        print("Yay {} is in the word.".format(letter_guess))
    else:
        print("Sorry fool")


def presentWord(word):
    # homework listOfStrings = []
    for t in word:
        print(t[0] if t[1] else " _ ", end='')


def createWordPule(word):

    return [(letter,False) for letter in word]


def loopGame():
    print("loopGame Run")

    # Initialize word.
    word = "michaelmos"
    wordPule = createWordPule(word)

    # Begin loop.
    guessCount = 0
    while True:
        presentWord(wordPule)
        checkGuess(guessWord(),wordPule)
        if didUserWin(wordPule):
            print("YOU WIN")
            break
        elif guessCount >= (len(word) + 4):
            print("YOU LOSE")
            break
        else:
            guessCount += 1


def promptForGameContinue():
    while True:
        s = input("type 'yes' or 'no': ")
        if s == "yes":
            return True
        elif s == "no":
            return False
        print(s + " is not an accepted answer.")

    #if "y" != input('Type "y" to Continue').lower():
    #    break


def main():
    while True:
        if not promptForGameContinue():
            break
        loopGame()

# Type 'yes' or 'no':
#   foo
# Type 'yes' or 'no':
#   yes
# ...
# Type 'yet' or 'no' to play again:
#   nope
# Type ';et' or 'no':
#   yes
# ...



if __name__ == '__main__':
    main()

#!=
'''
HIGHLEVEL
- Loop through game decision options
---- Accept entry of whether or not the person wants to play again
---- if yes:
-------- call loopGame()
---- else:
-------- end the game by breaking game decision loop


Def loopGame():
- Select a word
- Present word and gallows (should it go here?)
- Loop until player wins or loses:
---- Present word and body parts (should it go here also, or only?)
---- Accept guess of letter
---- Check if letter is in selected word
-------- If letter is in selected word
------------ If the player has guessed all of the letters in the word
---------------- Present the “You Win” message
---------------- break
-------- If letter is not in selected word
------------ If the player has guessed incorrectly 6 times
---------------- Present “Game Over” message
---------------- break

MIDDLE LEVEL
X Select a word
- From a table, select a list of words that have not been flagged as guessed
- Assign selected word to a list called "word"
- Split the word into tuples where the letter is the first element of the tuple
and "False" is the second element of the tuple.
- Present word and gallows (should it go here?)
- Print an em
- Loop until player wins or loses:
---- Present word and gallows (should it go here also, or only?)
---- Accept guess of letter
---- Check if letter is in selected word
-------- If letter is in selected word
------------ If the player has guessed all of the letters in the word
---------------- Present the “You Win” message
---------------- Present Do you want to play again message
------------ If the player has not guessed all of the letters in the word
---------------- Present all instances of letter in word, in their appropriate space
---------------- Accept guess of letter
-------- If letter is not in selected word
------------ If the player has guessed incorrectly 6 times
---------------- Present “Game Over” message
---------------- Present Do you want to play again message
------------ If the player has guessed incorrectly less than 6 times
---------------- Present next body part
---------------- Accept guess of letter
'''
