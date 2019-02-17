def guessWord():
    # homework eliminate this as a function
    letter_guess = input("Guess a letter").lower()

    return letter_guess


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
'''

# take input list 'wordPule' and generate output list.
# for every tuple in wordPule we make a new tuple. if the
# letter matches, we changed the Boolean to True. if
# letter doesn't match, we leave Boolean alone

#  'x'
#  ('l', True)      -> ('l', True)
#  ('l', False)     -> ('l', False)
#  ('x', True)      -> ('x', True)
#  ('x', False)     -> ('x', True)

# HOMEWORK Turn into a list comprehension
def checkGuess(letter, wordPule):
    output = []
    for le,bo in wordPule:
        if letter.lower() == le:
            output.append((le, True))
        else:
            output.append((le, bo))

    found = False

    for le, bo in wordPule:
        if letter.lower() == le:
            found = True

    if found == True:
        print("Nice job {} in the word".format(letter))

    else:
        print("Letter not in the word")

    return output


def presentWord(word):
    # homework listOfStrings = []
    # NOT: [<print, x=1, if <>: else:> for <something> in <something>]
    # YES: [<expression: x*x, x[0]> for <something> in <something>]
    #
    # [expression for item in list]

    # with an if statement, assign the displayed form of a letter to 'd'
    # input is tuple t
    list1 = [ le if bo else " _ " for le,bo in word]
    print("".join(list1))

    # print as "t _ s _ o"
    # "t, _ ,s, _ ,o"   "".join(list1)
    #print()
    #for t in word:
    #    print(t[0] if t[1] else " _ ", end='')



def createWordPule(word):

    return [(letter,False) for letter in word]


def loopGame():
    print("loopGame Run")

    # Initialize word.
    word = "michaelmos"
    # wordPule initialized here
    wordPule = createWordPule(word)

    # Begin loop.
    guessCount = 0
    while True:
        presentWord(wordPule)
        wordPule = checkGuess(guessWord(), wordPule)
        # checkGuess(guessWord(),wordPule)

        if all([v for l,v in wordPule]):  # Checks to see if the user won
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
