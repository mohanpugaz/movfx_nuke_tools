from matteEngine import matteEngine

Mn_Toolbar=nuke.toolbar("Mo Nodes")
Mn_Toolbar.addCommand('Mohan Tools/MatteEngine',lambda:matteEngine(),icon="M.jpg")

n=nuke.menu('Nuke')
n.addCommand('Mo_Tools/MatteEngine',lambda:matteEngine(),icon="M.jpg")

