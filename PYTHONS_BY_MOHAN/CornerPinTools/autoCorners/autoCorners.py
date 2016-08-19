import nuke

def autoCorners( node ):

    frame = nuke.frame()
    first = frame
    last = frame
    inc = 1
    layer = "rgba"

    selNode = nuke.selectedNode() 
    all_nodes = nuke.allNodes() 

    for i in all_nodes: 
        i.knob("selected").setValue(False) 

    selNode.knob("selected").setValue(True) 
    autocropper = nuke.createNode("CurveTool",'''operation 0 ROI {0 0 input.width input.height} Layer %s label "Processing Crop..." selected true''' % (str(layer), ), False) 

    nuke.execute(autocropper, first, last, inc) 
    autocropper.knob("selected").setValue(True) 
    autocropbox = autocropper.knob("autocropdata"); 
    cData = autocropbox.getValue()

    nuke.delete(autocropper)

    x=cData[0]
    y=cData[1]
    r=cData[2]
    t=cData[3]

    cpNode= node
    cpNode['from1'].setValue([x,y])
    cpNode['from2'].setValue([r,y])
    cpNode['from3'].setValue([r,t])
    cpNode['from4'].setValue([x,t])

    cpNode['to1'].setAnimated()
    cpNode['to2'].setAnimated()
    cpNode['to3'].setAnimated()
    cpNode['to4'].setAnimated()

    cpNode['to1'].setValue([x,y])
    cpNode['to2'].setValue([r,y])
    cpNode['to3'].setValue([r,t])
    cpNode['to4'].setValue([x,t])

        
