import getWord
import random

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

    def haveWon(self):
        hasWon = True
        for i in range(len(self.letterStatus)):
            if self.letterStatus[i][1] == False:
                hasWon  = False
        return hasWon

    def checkLetter(self, letterToCheck):
        isLetterInWord = False
        self.guessedLetters.append(letterToCheck)
        for i in range(len(self.letterStatus)):
            if self.letterStatus[i][0] == letterToCheck:
                isLetterInWord  = True
                self.letterStatus[i][1] = True
        return  isLetterInWord

    def didTheyGuess(self,letterCheck):
        if letterCheck in self.guessedLetters:
            return True
        else:
            return False


def initializeWordManager():
    """Initialize WordManager and return it."""
    mikeWord = getWord.getRandomWord()
    print("'{}'".format(mikeWord))
    newWord = WordManager(mikeWord)
    print(newWord.toGameString())
    return newWord

def playGame(w):
    wrongGuesses = 0

    while True:
        print(wrongGuesses)

        # this employee's job (this function) will be
        # to determine if it's a correct guess (alter 'w'
        # if so) and whether game has been won or lost
        #alreadyGuessed = True
        while True:
            guessedLetters = input("Guess a letter")
            if w.didTheyGuess(guessedLetters):
                print("you already guessed this letter, guess again")
            else:
                break

        isCorrect = w.checkLetter(guessedLetters) # delegate this to WordManager

        if isCorrect:
            print ("Awesome!!!")
        else:
            wrongGuesses += 1
            if wrongGuesses >= 3:
                print("You Lose")
                break
            else:
                print ("too bad, guess again")

        if w.haveWon():
            isWin = True
            print("You Win")
            break
            #return isWin
        #else:
            #isWin = False
            #return isWin


    # Check guessed letter to see if its in the word
    # If its in the word --> change all instances of letter in letterStatus to True
    # If its not in the word -->

# def finish(w, winFlag):
#    if winFlag:
#        print("YOU WIN!")
#    else:
#        print("YOU LOSE")
#
#    if input("Would you like to play again True/False?"):
#        main()
#    else:
#        break

def loadDictionary():
    # you want automatic clean up
    with open("engmix.txt", "rb") as f:
        #buffer = f.read()
        # "accused\naccumulate..."
        words = f.readlines()
    print(words[1000])
    return words


def main():

    while True:
        w = initializeWordManager()
        playGame(w)
        if theydontwanttoplayagain:
            break

    #finish(w, winFlag)

#wordup = WordManager("dog")
#print(wordup.toGameString())

main()
