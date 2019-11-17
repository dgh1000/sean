import re

text = '''
There will be food on the table. 
There will be presents on the table.

There will be food not on the table.

Rover ate cheese.
Fido ate cheese.
Rover ate hot dogs.
Fido ate hot dogs.

George ate hot dogs.
Fido ate hamburgers.


'''

def showAllMos(mos):
    for mo in mos:
        print(mo.group(0))

def test1():
    # what does this match and not match? verify.
    mos = re.finditer(r'food|presents', text)
    showAllMos(mos)


def test2():
    # what does this match and not match? verify
    mos = re.finditer(r'(food|presents) on the table', text)
    showAllMos(mos)

def test3():
    # CHALLENGE: one regex that matches all the lines from 9
    # to 12, but not 14 or 15
    pass

test1()
