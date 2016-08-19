import nuke
import nukescripts

def copyPremult():

    n=nuke.createNode('Copy')
    m=nuke.createNode('Premult')

    n['selected'].setValue(True)
    m['selected'].setValue(True)

    sel=nuke.selectedNodes()
    for i in sel:
        nuke.autoplace(i)
    
    nukescripts.clear_selection_recursive()
