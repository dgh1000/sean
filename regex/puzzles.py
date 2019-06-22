import re

def printStats(mo):
    print()
    if mo is None:
        print('no match object!')
        return
    gs = mo.groups()
    for i in range(len(gs) + 1):
        print('gr:{} start:{:8} end:{:8} | {}'.
              format(i, mo.start(i), mo.end(i), mo.group(i)))
    print()



# some wildcard characters you might need:
#
# .         match anything that's not a newline
# \w        match any alphnumeric character: numbers, letters, or underscore
# \d        match any digit
# \s        match any form of whitespace (spaces, tabs, newlines, return)
# [abcd]    a character set. matches any character inside the brackets (in
#           this case, 'a', 'b', 'c', or 'd')
# [a-z]     a form of character set which matches a range from 'a' to 'z'
# [^a-z]    a form of character set which matches anything NOT inside. This
#           would match Z, 1, _, etc. But not a, b, c, d, etc.
# \W        matches anything that's NOT alphanumeric
# \D        matches anything that's NOT a digit
# \S        matches anything that's NOT a whitespace



def puzzle1():
    # search and find a match from the first 't' in 'together' to the 'r' in
    # run. You're going to have a wildcard character like '.' in your regular
    # expression. You'll then modify it with a '*' or '+'. If you want to make
    # it non-greedy you'll add a further modifier to the end, '?'.
    #
    # Search for the Python 're' module and choose the official python
    # documentation for a 3.x version of Python. Look at the documentation for
    # these wildcards and modifiers.
    str1 = "together we run"
    matchString = 't.*r' # PUT YOUR SOLUTION HERE
    print(matchString)
    printStats(re.search(matchString, str1))


def puzzle2():
    # search from the 't' in together to the 'r' in together. Do this with a
    # non-greedy pattern.
    str1 = "together we run"
    matchString = 't.*r?' # PUT YOUR SOLUTION HERE
    printStats( re.search(matchString, str1) )

def puzzle3():
    # search from the 't' in together to the 'r' in together. Do this with a
    # *greedy* pattern but use a different wildcard character so that the
    # matches don't extend past the word together.
    str1 = "together we run"
    matchString = 't.+?' # PUT YOUR SOLUTION HERE
    printStats( re.search(matchString, str1) )

def puzzle4():
    str1 = "together we run. run."
    # find the entire first sentence up to but not including the period. use a
    # greedy expression but adjust the wildcard.
    matchString = "???" # PUT YOUR SOLUTION HERE
    printStats( re.search(matchString, str1) )

def puzzle5():
    str1 = 'this is a "quoted string 1234" outside'
    # find the double quoted string and everything inside. Capture what's
    # inside as a group (a group that exludes the quotes)
    matchString = "???" # PUT YOUR SOLUTION HERE
    printStats( re.search(matchString, str1) )


def puzzle6():
    str1 = 'yup. This is a sentence. and more.'
    str2 = 'okay. And another sentence. and more.'
    # write a regular expression that matches complete sentences starting with
    # a capital letter. Make sure it works for both sentences (in str1 and
    # str2). Have a group capture everything but the period.
    #
    # Note: you'll have to look up how to match a period, because normally a
    # period inside a regular expression is a wildcard.
    matchString = "???"
    printStats( re.search(matchString, str1) )
    printStats( re.search(matchString, str2) )

puzzle3()
