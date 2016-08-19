import nuke
from assign import addAssign,addAssignAuto,getInfos,main,addAssignManual,getFilePaths

nuke.addOnUserCreate(addAssignAuto,nodeClass=('Read'))
menu=nuke.menu('Nuke')
assignMenu=menu.addMenu('Mo_Tools/assign',icon="M.jpg")

assignMenu.addCommand('assign',lambda:main(),icon="assign.png")
assignMenu.addCommand('add assign tab to read',lambda:addAssignManual(),icon="addAssign.png")
assignMenu.addCommand('Get File Paths only',lambda:getFilePaths(),'alt+d',icon="M.jpg")

