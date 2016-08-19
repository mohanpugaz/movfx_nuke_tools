import nuke
from setCPRef import addSetRef , setRefToCurFrame
nuke.addOnCreate(addSetRef,nodeClass=('CornerPin2D'))

menu=nuke.menu('Nuke')

menu.addCommand('Mo_Tools/CornerPinTools/Set CP Ref frame', lambda:setRefToCurFrame(nuke.selectedNode())  , 'shift+f' , icon="M.jpg" )
