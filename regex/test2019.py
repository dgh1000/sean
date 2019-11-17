import re

gtext = """
B:W
sunny today in hell
E:W

John has a lot of chats on this line 
John has a lot of chats on smoke signal 
The dog needs a $TOKEN to game
The dog needs a %TOKEN to game
The dog needs a TOKEN to lame
"""

gtext2 = '456\n123 there'

def testNov11():
    # find "chats on this line" or "chats on this smoke signal"
    #
    # TOKEN. $TOKEN  %TOKEN   don't want to find: TOKEN
    listy = re.finditer(r'\$TOKEN|\%TOKEN',gtext,re.DOTALL )
    
    for mo in listy:
        print(mo.group(0))

def searchString(regx, text):
    mo = re.search(regx,text)
    return mo

def searchForWeather():
    print(re.search(r'B:W.*E:W', gtext, re.DOTALL))

#searchForWeather()
testNov11()
