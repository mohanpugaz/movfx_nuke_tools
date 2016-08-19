#TEST TEST TEST

n=nuke.selectedNode()

redv   =n['red'].getValue()
greenv =n['green'].getValue()
blue   =n['blue'].getValue()
alpha  =n['alpha'].getValue()

if redv==1.0:
    labelRed="Red to Red"
if redv==2.0:
    labelRed="Green to Red"
if redv==3.0:
    labelRed="Blue to Red"
if redv==4.0:
    labelRed="Alpha to Red"
if redv==5.0:
    labelRed="Red None"
if redv==6.0:
    labelRed="Red Fill"
    

if greenv==1.0:
    labelGreen="Red to Green"
if greenv==2.0:
    labelGreen="Green to Green"
if greenv==3.0:
    labelGreen="Blue to Green"
if greenv==4.0:
    labelGreen="Alpha to Green"
if greenv==5.0:
    labelGreen="Green None"
if greenv==6.0:
    labelGreen="Green Fill"

if bluev==1.0:
    labelGreen="Red to Green"
if bluev==2.0:
    labelBlue="Green to Green"
if bluev==3.0:
    labelBlue="Blue to Green"
if bluev==4.0:
    labelBlue="Alpha to Green"
if bluev==5.0:
    labelBlue="Green None"
if bluev==6.0:
    labelBlue="Green Fill"


node=labelRed+labelGreen+labelBlue
