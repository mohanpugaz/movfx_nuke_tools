import nuke


def hideinput():
    
    n=nuke.selectedNodes()
    for node in n:
            node.knob('hide_input').setValue(True)

menubar=nuke.menu("Nuke")

Mn_Toolbar=nuke.toolbar("Nodes")

addCommand("Hide Input","nuke.createNode(\"hideinput\")",icon="M.jpg")


