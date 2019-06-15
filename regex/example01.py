
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


data2 = \
"""<header><>
  <nav class="navbar navbar-default">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" 
                data-target="#myNavbar">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <!-- a class="navbar-brand" href="#">WebSiteName</a -->
      </div>
      <div class="collapse navbar-collapse" id="myNavbar">
        <ul class="nav navbar-nav">
          <li><a href="index.html">Home</a></li>
          <li class="dropdown">
            <a class="dropdown-toggle" data-toggle="dropdown" href="#">Ideas</a>
            <ul class="dropdown-menu">
              <li><a href="ideas/babysteps.html">Baby steps</a></li>
            </ul>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="contact.php">Contact</a></li>
        </ul>
      </div>
    
  </nav>
</header>
"""

def printStats(mo):
    if mo is None:
        print('no match object!')
        return
    gs = mo.groups()
    for i in range(len(gs) + 1):
        print('gr:{} start:{:8} end:{:8} | {}'.
              format(i, mo.start(i), mo.end(i), mo.group(i)))
              

def startSimple01():
    mo = re.search(r'confronted', data1)
    print('{}'.format('None' if mo is None else mo.group(0)))

    
def startSimple02():

    mo = re.search(r'c[oh]', data1)
    print('{}'.format('None' if mo is None else mo.group(0)))
        

def test01():
    print('\nExperiment 1:')
    mo = re.search(r'She', data1)
    printStats(mo)

    print('\nExperiment 2:')
    mo = re.search(r'Sce', data1)
    printStats(mo)

    print('\nExperiment 3:')
    mo = re.search(r'S.e', data1)
    printStats(mo)

    
def test02():
    print('\nExperiment 1:')
    mo = re.search(r'es*', data1)
    printStats(mo)
    
    print('\nExperiment 2:')
    mo = re.search(r'es+', data1)
    printStats(mo)

    print('\nExperiment 3:')
    for mo in re.finditer(r'es+', data1):
        printStats(mo)


def test03():
        
    print('\nExperiment 1:')
    for mo in re.finditer(r'1.*9', data1):
        printStats(mo)
        
    print('\nExperiment 2:')
    mo = re.search(r'\d', data1)
    printStats(mo)

    print('\nExperiment 3:')
    mo = re.search(r'\d+', data1)
    printStats(mo)

def test04():
    print('\nExperiment 1:')
    for mo in re.finditer( r'<a clas.*>', data2):
        printStats(mo)
        

    print('\nExperiment 2:')
    for mo in re.finditer( r'<a clas.*?>', data2):
        printStats(mo)

    print('\nExperiment 3:')
    for mo in re.finditer( r'<a clas.*?>', data2):
        printStats(mo)
        
        
startSimple02()
