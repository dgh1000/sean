# concern : how do we represent the word along with an indication of what letters have been guessed?

wordier = [("m", True), ("i", False), ("c", True), ("h", False), ("a", True), ("e", True), ("l", False)]
#print(word)

#print([2*i for i in range(15) if i%2 == 0])
#print([t[0] for t in word if t[1] == True])

# loop that prints either the character or " _ " depending on flag value
def wordpresent(word):
    for t in word:
        print(t[0] if not t[1] else " _ ")
# x = 7 if len(wordier) > 4 else (2 if len(wordier) < 2) else 10)

# x == 7

wordpresent(wordier)

def wordchannukah(word):
    w = [t[0] if not t[1] else " _ " for t in word]
    print("".join(w))

wordchannukah(wordier)
print("".join(["s", "e", "a", "n"]))

v = "this"
print(v.join(list("hello")))
# 2nd u se of join: Girder(), join(girder1, girder2)


'''
HIGHLEVEL
- Loop through game decision options
---- Accept entry of whether or not the person wants to play again
---- if yes:
-------- call gameloop()
---- else:
-------- end the game by breaking game decision loop


Def gameloop():
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
