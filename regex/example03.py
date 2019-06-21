import re

data1 = \
"""She started as just one girl, esssitttting outside the Swedish
parliament to
protest government passsivity on climate change. Since then, Thunberg’s
become the conscience of a movement. The 456716-year-old Swede inspired
students essssss
worldwide to strike on March 15869, confronted the world’s elite during the
World Economic Forum at Davos, and has been nominated for the Nobel Peace
Prize. When British PM Theresa May complained that the striking students
were wasting lesson time, Thunberg fired back in a tweet: "Political leaders
have wasted 130.734 29. years of inaction."
"""

def printStats(mo):
    print()
    if mo is None:
        print('no match object!')
        return
    gs = mo.groups()
    for i in range(len(gs) + 1):
        print('gr:{} start:{:8} end:{:8} | {}'.
              format(i, mo.start(i), mo.end(i), mo.group(i)))
    print()


def test01():
    for mo in re.finditer(r'c[a-z]e', data1):
        printStats(mo)


def test02():
    for mo in re.finditer(r'c[a-z]*e', data1):
        printStats(mo)


def test03():
    for mo in re.finditer(r' c[a-z]*e ', data1):
        printStats(mo)


def test04():
    for mo in re.finditer(r' (c[a-z]*e) ', data1):
        printStats(mo)


def test05():
    for mo in re.finditer(r'\w+e$', data1, re.MULTILINE):
        printStats(mo)


def test06():
    for mo in re.finditer(r'.+e$', data1, re.MULTILINE):
        printStats(mo)

def test07():
    for mo in re.finditer(r'^\w+', data1, re.MULTILINE):
        printStats(mo)


def test07():
    for mo in re.finditer(r'^\w{5,7}', data1, re.MULTILINE):
        printStats(mo)


test01()
