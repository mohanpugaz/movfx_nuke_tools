from Mo_RotoTools import cpToMatrixMenu,stablizeFromRotoLayer,addMoTab,dieBefore,dieAfter,singleFrame
from RemoveRotoBlurs import removeBlurs

nuke.addOnUserCreate(addMoTab,nodeClass='Roto')
nuke.addOnUserCreate(addMoTab,nodeClass='RotoPaint')

menu=nuke.menu('Nuke')
rotoMenu=menu.addMenu('Mo_Tools/Roto', icon = "roto.png")
rotoMenu.addCommand('DieBefore',lambda:dieBefore(),'alt+v',icon="M.jpg")
rotoMenu.addCommand('DieAfter',lambda:dieAfter(),'alt+b',icon="M.jpg")
rotoMenu.addCommand('Swap',lambda:singleFrame(),'alt+y',icon="M.jpg")
rotoMenu.addCommand('OFF Roto Feather And MB',lambda:removeBlurs(nuke.selectedNode()),icon="M.jpg")
#menu.addCommand('Mo_Tools/CornerPin To Matrix',lambda:cpToMatrixMenu(),icon="M.jpg")
#menu.addCommand('Mo_Tools/Stablize From Roto Layer',lambda:stablizeFromRotoLayer(nuke.selectedNode()),icon="M.jpg")
