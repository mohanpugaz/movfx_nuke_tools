import nuke
from autoCorners import autoCorners


menu=nuke.menu('Nuke')
menu.addCommand('Mo_Tools/CornerPinTools/Autocorners',lambda:autoCorners(nuke.createNode('CornerPin2D')) , icon="M.jpg" )


