import nuke

def setRefToCurFrame(node):
    n=node
    frame=nuke.frame()

    fromOne=n['from1']
    fromTwo=n['from2']
    fromThree=n['from3']
    fromFour=n['from4']

    toOne=n['to1'].getValue()
    toTwo=n['to2'].getValue()
    toThree=n['to3'].getValue()
    toFour=n['to4'].getValue()

    fromOne.clearAnimated()
    fromTwo.clearAnimated()
    fromThree.clearAnimated()
    fromFour.clearAnimated()
    
    fromOne.setValue(toOne)
    fromTwo.setValue(toTwo)
    fromThree.setValue(toThree)
    fromFour.setValue(toFour)
    
    result = "cornerPin reference frame set to frame %s" % frame
    
    return result

def addSetRef():
    node=nuke.thisNode()
    newTab=nuke.Tab_Knob('M_tab') 
    newKnob=nuke.PyScript_Knob("SetRef","setRef","setRefToCurFrame(nuke.thisNode())")
    node.addKnob(newTab)
    node.addKnob(newKnob)
    return None




