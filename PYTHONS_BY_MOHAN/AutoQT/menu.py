from autoQT import AutoQT

Mn_Toolbar=nuke.toolbar("Mo Nodes")
Mn_Toolbar.addCommand('Mohan Tools/AutoQT',lambda:AutoQT(),'shift+q',icon="M.jpg")

n=nuke.menu('Nuke')
n.addCommand('Mo_Tools/AutoQT',lambda:AutoQT(),'shift+q',icon="M.jpg")
