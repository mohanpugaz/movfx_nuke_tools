import nuke

def bboxCorners( node ):

    n=nuke.selectedNode()
    
    x = n.bbox().x()
    y = n.bbox().y()
    r = (n.bbox().x())+(n.bbox().w())
    t = (n.bbox().y())+(n.bbox().h())

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

        
