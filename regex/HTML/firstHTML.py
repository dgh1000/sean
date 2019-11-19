import re

htmlstr = '''
<div>
<p>Duff got his hair did today</p>
<p>and I had to do some additional cuts</p>
</div>
'''

# 'some words \n '
# 'something\\somethingelse'
# 'some\\thing\\here\\is\\taking\\a\\lot\\of\\chars'
# '\\s\\$(\\w)+'
# r'\s\$(\w)+'
# 'some chars'
# print(s)
# print('some chars') 

def parseALL(string,typeName):
    reExp = r"'<" + typeName + r">(.*?)</" + typeName + r">'"
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
    parseALL(htmlstr, "div")
    #parseP(htmlstr)
    #parseDIV(htmlstr)


main()