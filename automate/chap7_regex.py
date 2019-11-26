import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        texttest = text[i]
        if not texttest.isdecimal():
            return False

    if text[3] != "-":
        return False

    for j in range (4,7):
        if not text[j].isdecimal():
            return False
    
    if text[7] != "-":
        return False

    for k in range(8,12):
        if not text[k].isdecimal():
            return False

    return True

def isPhoneNumberRE(text):
    regexChecker = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print("in RE")
    #if regexChecker.search(text):
    #    return True

    mo = regexChecker

#print("not a phone number")
#print("phone number")

def main():
    numberToTest = "323-632-8811"
    if isPhoneNumberRE(numberToTest):
        print("phone number")
    else: 
        print("not a phone number")

main()
