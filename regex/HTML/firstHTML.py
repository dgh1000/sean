import re

htmlstr = '''
<div id="duff" class="doggy" style="yadda">
<p>Duff got his hair did today</p>
<p>and I had to do some additional cuts</p>
</div>
'''

attrStr2 = 'id="duff" class="doggy" style="yadda"'
# .*?=
# \w*? alphanumeric ->   id,   not match id=
# find iter on attrStr1



htmlstrPD = '''
<p>P-element First</p>
<div>
</div>
<p>P-element Last</p>
'''

# 'some words \n '
# 'something\\somethingelse'
# 'some\\thing\\here\\is\\taking\\a\\lot\\of\\chars'
# '\\s\\$(\\w)+'
# r'\s\$(\w)+'
# 'some chars'
# print(s)
# print('some chars') 


def searchAttrStr1():
    attrRegex = re.compile(r'(\w+)="(\w+)"')
    attrStr1 = 'blah="someElement" class="doggy" style="yadda"'
    molist = attrRegex.finditer(attrStr1)
    # [], [<mo 1>], [<mo 2>, <mo 3>, ... ]

    if molist:
        for mo in molist:
            print(mo.group(1))
            print(mo.group(2))
    else:
        print("None Found")
        # abc = [ 'abc', 3, 'x']
        # for value in abc:
        #     <body>
        #
        # value: 
        #   'abc'
        #   3
        #   'x'


    # printMO(mo)

def removeNewlines(string):
    '''The function takes a string and returns the string without newline chars'''
    s = re.sub('\n','',string)
    return s

def parseAB (string):
    # '<p>(.*?)</p>'
    # '<(.*?)>(.*?)</\1>'
    reExp = r'<(.*?)>(.*?)</\1>'
    mo = re.search(reExp, string, re.DOTALL)
    printMO(mo)

def parseALL(string,typeName):
    reExp = r'<' + typeName + r'>(.*?)</' + typeName + r'>'
    mo = re.search(reExp, string, re.DOTALL)
    printMO(mo)

def parseP(string):
    moP = re.search(r'<p>(.*?)</p>',string,re.DOTALL)
    printMO(moP)

def parseDIV(string):
    moDIV = re.search(r'<div>(.*?)</div>',string,re.DOTALL)
    printMO(moDIV)


def printMO(mo):
    if mo:
        print(mo.group(1))
    else:
        print('Nothing here idiot')


def main():
    #parseAB(removeNewlines(htmlstr))
    #parseAB(removeNewlines(htmlstrPD))
    #parseALL(htmlstrPD, "div")
    #parseALL(htmlstrPD, "p")
    #parseP(htmlstr)
    #parseDIV(htmlstr)
    searchAttrStr1()


main()