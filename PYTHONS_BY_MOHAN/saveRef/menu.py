from saveRef import find_upstream_node,saveRef
menu=nuke.menu('Nuke')
menu.addCommand('Mo_Tools/Save Ref',lambda:saveRef(),'alt+shift+r',icon="m_icon.jpg")
