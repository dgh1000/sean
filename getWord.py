import random

def getRandomWord():
    with open("engmix.txt", "rb") as f:
        lines = f.readlines()

    linesD = []
    for l in lines:
        try:
            x = l.decode("utf-8")
            linesD.append(x)
        except:
            pass

    return random.choice(linesD)
