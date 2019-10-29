import re

gtext = """
Mike jumps over the lazy dog
and can be reached at 555-5555 more on this line

B:W
sunny today in hell
E:W


1-234-2342342-23
10.123.1234.1356
888-888-8888

18.2NW36.3SE5
"""

gtext2 = '456\n123 there'

def searchString(regx, text):
    mo = re.search(regx,text)
    return mo

#print(searchString("ike",gtext))

# regard it as a series of characters drawn from the set 0,..,9,.,-
# r"()

#for mo in re.finditer(r".+",gtext2):
#    print(mo)

def searchForWeather():
    print(re.search(r'B:W.*E:W', gtext, re.DOTALL))

searchForWeather()
