#
# examples of expressions, values, and function calls
#
# 

def addOne(x):
    y = 3
    return x+1

def makeList(x):
    return [x, x, x]

def sumList(l):
    result = 0
    for x in l:
        result += x
    return result

def modifyList(l):
    l[0] = -1

# ----------------------------------------------------------------------
# some "main" functions (entry points for execution of test code)

def main1():
    y = 5
    print(addOne(2))
    print(y)


def main2():
    x = makeList(1)
    y = makeList(2)
    print([x, y])
    print([makeList(1), makeList(2)])

def main3():
    print(sumList([1, 2, 3]))

def main4():
    print(sumList(makeList(5)))

def main5():
    # this is the one example in which a function mutates data contained
    # in part of the structure passed to it in an argument.
    x = makeList(1)
    print(x)
    # the following function call mutates the list in 'x'
    modifyList(x)
    print(x)

    
# uncomment the "main" function you want to run

main1()
#main2()
#main3()
#main4()
#main5()


