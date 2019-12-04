import re

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


attrStringTest1 = '''
    <div id="someid" class="someclass"> blah </div>
'''

attrStringTestNONE = '''
'''
htmlstr = '''
<div id="duff" class="doggy" style="yadda">
<p>Duff got his hair did today</p>
<p>and I had to do some additional cuts</p>
</div>
<div id="second div" class="second class" style="second style">
'''

def search_for_tags():
    search_string = r'<(\w+)\s(.*)>'
    complier = re.compile(search_string)
    # mo = complier.findall(htmlstr)
    #print(complier.findall(htmlstr)[0][1])

    #print(mo.group())
    attribute_search_string = r'(\w+)="(.*)"'
    complier2 = re.compile(attribute_search_string)
    #mo2 = complier2.findall(mo[0])

    print(complier2.findall(complier.findall(htmlstr)[0][1]))


    # if mo:
    #    print(mo.group(0))
    #    print(mo.group(1))
    #    print(mo.group(2))
        # print(mo.group(3))
    #else:
    #    print("None Case")

    #if mo2:
    #    print(mo2.group(0))
    #    print(mo2.group(1))
    #    #print(mo2.group(2))
        # print(mo.group(3))
    #else:
    #    print("None Case")


def searchForOpeningTag():
    # '[here be non-repeating part][here be repeating part]*'
    reStructure = r'<(\w+)\s(\w+="(\w+)"\s*)*>'
    openTag = re.compile(reStructure, re.DOTALL)
    # openTag = re.compile(r'(<(.+?)>)')
    # mo = openTag.search(attrStringTest1)
    mo = openTag.search(htmlstr)

    if mo:
        print(mo.group(0))
        print(mo.group(1))
        print(mo.group(2))
        print(mo.group(3))
    else:
        print("None Case")
    
    # for mo in molist:
        # print(mo.groups())
        # print(mo.group(2))

def searchAttrStr1():
    attrRegex = re.compile(r'(\w+)="(\w+)"', re.DOTALL)
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

def main():
    # searchAttrStr1()
    # searchForOpeningTag()
    search_for_tags()


main()