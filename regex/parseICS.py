import re

def loadText():
    fileName = "sampleICS.txt"
    with open(fileName, "r") as f:
        buf = f.read()
        
    return buf

def findOneEvent(buf):
    '''Given text, this function searches through the text and finds all
    instances of each event based on their beginning and ending tags
    
    In its current configuration, this function searches for BEGIN:VEVENT to
    denote the beginning of an event and END:VEVENT to denote the end.
    
    The function returns the first event as an match object'''

    # mo = re.search(r"BEGIN:VEVENT.*?END:VEVENT",buf, re.DOTALL)
    mos = re.finditer(r"BEGIN:VEVENT.*?END:VEVENT",buf, re.DOTALL)
    # we would expect mo is a list

    moList = list(mos)
    firstMo = moList[0]
    return firstMo
    
def parseEvent(matchObject):
    '''Given a match object, this function searches for one or more elements
    within that match object's text.

    In the current instance, this function searchs for a single element: summary.
    Summary is denoted by a leading SUMMARY: and a TRAILING DTSTART.  
    
    The function prints to the terminal the summary section of the event.
    '''
    moStr = matchObject.group(0)
    summaryMO = re.search(r"SUMMARY:(.*?)DTSTART", moStr, re.DOTALL)
    # meaning of mo.group(n) : mo.group(0) is the entire matching string
    # mo.group(1) is the matching portion within the first capturing group
    # mo.group(n) is the matching portion within the nth capturing group

    print(summaryMO.group(1))

    # here we're going to call sub on group(1)
    text = re.sub(r'\n ', '', summaryMO.group(1))
    print(text)

def main(): 
    # The application takes in a well structured file, with regularly repeated 
    # elements E.
    # Within each E, the system then seeks for specific sub-elements S1, S2, .. Sn.  

    # In this specific case, E is sections beginning and ending with VEVENT.
    # We seek S1, "SUMMARY".

    # It then
    # presents those elements to the user...and changes their lives in the doing.
    
    buf = loadText()
    ev = findOneEvent(buf)
    parseEvent(ev)
    # if ev:
    #     with open('out.txt', 'w') as f:
    #         f.write(ev)
    # else:
    #     print('no match')

main()

