
class WordPule:

    def __init__(self, chars):
        # chars "antidisestablishmentarism"
        # self.tuples = [["a", False], ["b", True]]
        self.stringy = [[x, False] for x in chars]
        print(self.stringy)

    def __str__(self):
        return str(self.stringy)

    def toGameString(self):
        # return " ".join(<list>)
        # --> ["d", False]
        return " ".join([i if j else "_" for i,j in self.stringy])

        #return "b _ n _ n _ "


    def numGuessed(self):
        """returns number of successfully guessed letters"""
        pass

    def wordLength(selfs):
        """return number of characters"""
        pass

    def setLetter(self, letter):
        """mutates self.tuples"""
        pass

    def haveWon(self):
        hasWon = True
        for i in range(len(self.stringy)):
            if self.stringy[i][1] == False:
                hasWon  = False
        return hasWon

    def checkLetter(self, letterToCheck):
        isLetterInWord = False
        for i in range(len(self.stringy)):
            if self.stringy[i][0] == letterToCheck:
                isLetterInWord  = True
                self.stringy[i][1] = True
        return  isLetterInWord

def getWord():
    return "mike"



def start():
    """Initialize WordPule and return it."""
    newWord = WordPule(getWord())
    print(newWord.toGameString())
    return newWord

def loop(w):
    wrongGuesses = 0

    while True:
        print(wrongGuesses)
        guessedLetter = input("Guess a letter")
        # this employee's job (this function) will be
        # to determine if it's a correct guess (alter 'w'
        # if so) and whether game has been won or lost
        isCorrect = w.checkLetter(guessedLetter) # delegate this to WordPule

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
    # If its in the word --> change all instances of letter in stringy to True
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

def main():
    # instantiate a WordPule and manipulate it to run the game
    w = start()
    winFlag = loop(w)
    #finish(w, winFlag)

#wordup = WordPule("dog")
#print(wordup.toGameString())

main()
