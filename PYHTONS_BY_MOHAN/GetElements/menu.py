import nuke
from getElements import getElements,getPath


mm=nuke.menu('Nuke')
m=mm.addMenu('Mo_Tools',icon="M.jpg")
m.addCommand('Get Elements',lambda:getElements(),icon="M.jpg")
