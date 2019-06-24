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

multiLine_01 = \
'''a string that has
multiple lines in in
and one more'''

multiLine_02 = 'a string that has\nmultiple lines in it\nand one more'

def testTripleQuotes():
    print('*** multiLine_01 ***')
    print(multiLine_01)
    print('*** multiLine_02 ***')
    print(multiLine_02)

def puzzle1():
    # search and replace all white space with a single space

    # note: two versions of the same string here, one using triple quotes and
    # one using
    str1_a = '''together
we run'''
    str1_b = 'together\nwe run'
    str1_c = 'together  we  run'
    strOut = re.sub(r'\s+', ' ', str1_c)
    print(strOut)


def puzzle2():
    # match 'foo' OR 'bar'
    str1 = 'foo bar&foo... bar'
    matchString = r'foo|bar' # PUT YOUR SOLUTION HERE
    for mo in re.finditer(matchString, str1):
        printStats(mo)

def puzzle3():
    # match exactly 2 consecutive repetitions of x
    str1 = 'tttt xx x tttxxx'
    matchString = r'x{2}' # PUT YOUR SOLUTION HERE
    for mo in re.finditer(matchString, str1):
        printStats(mo)

    
def puzzle3_b():
    # match between 2 and 4 consecutive repetitions of x
    str1 = 'tttt xx x tttxxx xxxxx xxxx'
    matchString = r'x{2,4}' # PUT YOUR SOLUTION HERE
    for mo in re.finditer(matchString, str1):
        printStats(mo)

    
def puzzle4():
    # match 2 repetitions of 'foo' OR 'bar'
    str1 = 'foo barbar bar&foobar... bar'
    matchString = r'???' # PUT YOUR SOLUTION HERE
    for mo in re.finditer(matchString, str1):
        printStats(mo)


def puzzle5():
    # substitute 'foo' with 'foofoo', and 'bar' with 'barbar'
    str1 = 'foo bar x... foofoo'
    str2 = re.sub(r'(foo|bar)', r'\1\1', str1)
    print(str2)



puzzle5()


