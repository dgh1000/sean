import getWord
import random
import re

def getRandomWord():
    with open("engmix.txt", "rb") as f:
        lines = f.readlines()

    decodedLines = []
    for l in lines:
        try:
            x = l.decode("utf-8")
            decodedLines.append(x)
        except:
            pass

    return random.choice(decodedLines)


class WordManager:

    def __init__(self, chars):
        # chars "antidisestablishmentarism"
        # self.tuples = [["a", False], ["b", True]]
        self.letterStatus = [[x, False] for x in chars]
        self.guessedLetters = []
        print(self.letterStatus)

    def __str__(self):
        return str(self.letterStatus)

    def toGameString(self):
        # return " ".join(<list>)
        # --> ["d", False]
        return " ".join([i if j else "_" for i,j in self.letterStatus])
        #return "b _ n _ n _ "

    def userHasWon(self):
        for i in range(len(self.letterStatus)):
            if self.letterStatus[i][1] == False:
                return False
        return True

    def updateLetter(self, guessedLetter):
        isLetterInWord = False
        self.guessedLetters.append(guessedLetter)
        for i in range(len(self.letterStatus)):
            if self.letterStatus[i][0] == guessedLetter:
                isLetterInWord  = True
                self.letterStatus[i][1] = True
        return  isLetterInWord

    def alreadyGuessed(self,guess):
        return guess in self.guessedLetters


def initializeWordManager():
    """Initialize WordManager and return it."""
    mikeWord = getWord.getRandomWord()
    print("'{}'".format(mikeWord))
    newWord = WordManager(mikeWord)
    print(newWord.toGameString())
    return newWord

def playGame(w):
    """Run through a game loop for one game.

    input arguments:
    - w: WordManager containing word for the game

    return value:
    - None.
    """
    wrongGuesses = 0

    while True:
        print(wrongGuesses)

        while True:
            guessedLetters = input("Guess a letter")
            # what makes input correct? one letter. not previously guessed.

            # match or extract information from strings
            #
            # prompt the user for a name: validate the input... all letters,
            # first was capital, . read a file of comma-separated numbers,
            # find stretches of numbers, find comma separating them, etc.
            # or more complex: read formatted data, search for patterns in
            # text files.
            #
            # validate that an input is a single letter.
            #
            # pick a letter and write it here: _

            # "[a-z]"
            # [a-z]           foo
            #  [a-z]         not match ""
            # [a-z]          not match "1a"

            # re.match returns a MatchObject which allows us to ask questions
            # about the match
            flag = re.match("[a-z]$", guessedLetters)
            if w.alreadyGuessed(guessedLetters):
                print("you already guessed this letter, guess again")
            elif flag:
                break

        isCorrect = w.updateLetter(guessedLetters) # delegate this to WordManager

        if isCorrect:
            print ("Awesome!!!")
        else:
            wrongGuesses += 1
            if wrongGuesses >= 3:
                print("You Lose")
                break
            else:
                print ("too bad, guess again")

        if w.userHasWon():
            isWin = True
            print("You Win")
            break

def main():

    while True:
        w = initializeWordManager()
        playGame(w)
        if theydontwanttoplayagain:
            break

main()
