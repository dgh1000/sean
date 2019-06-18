import re

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
        
        
def test05():
    mo = re.search( r'<(\w+).*?>', data2)
    printStats(mo)
    
test05()
