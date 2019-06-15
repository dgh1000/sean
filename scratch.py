import re


def helloWorld():

    s = "There is this thing called TestValue is a sentence. TestValue"
    s2 = "bd"
    s3 = "bed"

    flag = re.search(r"b.*d", s2)

    if flag:
        print(flag.group(0))
    else:
        print("No match")

def searchAll():

    s = "bedd x beadddd x baddd x bdooboo"
    x = 3*4
    x = (3*4)

    matches = re.finditer(r"b([ae]*)(d+)", s)

    for m in matches:
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))


#helloWorld()
searchAll()
