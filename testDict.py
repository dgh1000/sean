
def tryDecode(l):
    try:
        return l.decode('utf-8')
    except:
        return None

with open("engmix.txt", "rb") as f:
    lines = f.readlines()

linesD = []
for l in lines:
    try:
        x = l.decode("utf-8")
        linesD.append(x)
    except:
        pass

print(linesD[50001])
