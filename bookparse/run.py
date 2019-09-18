bookFileName = 'jj_pofa_p1.txt'

def readBook(fileName):
    with open(fileName, 'rb') as f:
        text = f.read()

    return text

def main():
    s = readBook(bookFileName)
    print(s[0:100])
    str.split()


main()
