'''
Expression in english

loop over data:



simplifying assumptions  >>> expression that has a value
'''

# data: abstraction
#
# low level: use binary data, binary : represent numbers
#
#     - characters A-Z, numbers vary in size (large or small),
#       floating point or integers, represnt some kind of choice
#       (holding a rifle or flamethrower)
#
# variable X holds the character "C"
#
#  7+8  :
#
# expression: several things that combine according to the rules
#
# structures: [1, 2, 3, 4]
#  x, y, w, z
#
# number of players.
#
#   list: maintains the values in a specific order, can be accessed by numeric
#   index
#
#   dictionary: { "left": 3, "right": 7}
#
#   set:


#romanNumeralLists = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
#                        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
#                        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]]

def genpattern(a,b,c):
    return["",a,a+a,a+a+a,a+b,b,b+a,b+a+a,b+a+a+a,a+c]

romanNumeralLists = [genpattern("I", "V", "X"),
                    genpattern("X","L", "C"),
                    genpattern("C", "D", "M")]

#rnl = [generatePattern, generatePat
#rnl[0]("I", "V", "X")

def computeDigits(n):
    """Return list of digits from ones places upward, any number digits"""
    # n= 345, output = [5, 4, 3]
    out = []
    while n > 0:
        out.append(n%10)
        n = n//10

    return out

def romanize():
    num = int(input("Enter number: "))
    rom = computeDigits(num)
    outy = ""

    # outy: translated into machine code, the name is lost. becomes a memory
    # address. 0x11117889.
    #
    # variableName = "outy"
    if len(rom) > 3:
        print("Enter a number with less than 4 digits")
    else:
        for i in range(len(rom)):
            outy = romanNumeralLists[i][rom[i]] + outy

        print(outy)








    #ones = num%10
    #tens = (num%100)//10
    #huns = (num%1000)//100

    # check if there a ones digit, in  clude the rns for ones digit
    # check if there is a tens digit, include those
    # check if there is a hundreds, include those

    #print(r100[rom[2]] + r10[rom[1]] + r1[rom[0]])


#print(computeDigits(int(input("Enter Num: "))))

romanize()

"""
# 707: hundreds(7) + tens(0) + ones(7)
n
outputValue = n%10     # ones place
n = n // 10
nextOutputValue = n%10  # tens place
n = n // 10
nextNextOutputValue = n%10  # hundreds place


"""




'''
I V X L C D M
0 1 2 3 4 5 6
numerals = ["I", "V", "X", "L", "C", "D", "M"]
numerals[0]  is "I"
numerals[1]  is "V"
numerals[2]  is "X"
numerals[3]  is "L"
numerals[4]  is "C"
numerals[5]  is "D"
numerals[6]  is "M"


7  : VII  : 1, 0, 0 numerals[1] + numerals[0] + numerals[0]
70 : LXX  : 3, 2, 2
700: DCC  : 5, 4, 4

77  : LXXVII : concatenation of representation of 70 and 7
770 : DCCLXX : (700 and 70)
707 : DCCVII : (700 and 7)





I"" <<<
"" <<<
""I
""II
""III

IV
V
VI
VII
VIII

012:

01         : IV  <<<
1          : V
10         : VI
100        : VII
1000       : VIII
02         : IX  <<<
2          : X
20         : XI
200        : XII
2000       : XIII
201        : XIV  <<<
21         : XV
210        : XVI
2100       : XVII
21000      : XVIII
202
22
220
2200

IX
X
XI
XII
XIII
XIV
XV
XVI
XVII
XVIII
XIX
XX
XXI
XXII
XXIII
XXIV
XXV
XXVI
XXVII
XXVIII
XXIX
XXX



 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20

    b1 = Box()
    b2 = Box()
    b3 = Box()
    #write code referencing b1, b2, b3

    boxes = []
    boxes.append(Box()) # reference at index 0
    boxes.append(Box()) # index 1

    boxes = {}
    boxes["b1"] = Box()
    boxes["b2"] = Box()


'''
