
class WordPule:


    def __init__(self, chars):
        # chars "antidisestablishmentarism"
        # self.tuples = [["a", False], ["b", True]]
        self.stringy = [[x, False] for x in chars]

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

def loop():
    # instantiate a WordPule and manipulate it to run the game
    pass

wordup = WordPule("dog")
print(wordup.toGameString())
