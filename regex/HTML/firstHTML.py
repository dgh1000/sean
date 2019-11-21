import re

htmlstr = '''
<div id="duff" class="doggy" style="yadda">
<p>Duff got his hair did today</p>
<p>and I had to do some additional cuts</p>
</div>
'''

attrStr1 = 'id="duff" class="doggy" style="yadda"'
# .*?=
# \w*? alphanumeric ->   id,   not match id=
# find iter on attrStr1

attrStr2 = 'id="duff"'


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
        print(mo.groups())
    else:
        print('Nothing here idiot')


def main():
    #parseAB(removeNewlines(htmlstr))
    parseAB(removeNewlines(htmlstrPD))
    #parseALL(htmlstrPD, "div")
    #parseALL(htmlstrPD, "p")
    #parseP(htmlstr)
    #parseDIV(htmlstr)


main()