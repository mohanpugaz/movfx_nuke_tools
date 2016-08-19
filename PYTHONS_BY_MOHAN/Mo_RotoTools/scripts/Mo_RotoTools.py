import nuke
import nukescripts

def cpToMatrix(targetNode,sourceNode):
        input = sourceNode
    
        #----------------------------------------------------------------------------------------------------------
 
        if  input.Class() == 'CornerPin2D':
          
            target=targetNode
            targetKnob=target.knob('transform_matrix')
           
            
             #---------------------------------------------------------------------------------------
            
            # conversion cp_to_mtx
            
            def getAnimatedCPasMTX(cornerpin, iterator):
                
                i = iterator
                cp =  cornerpin
                
                pmTo = nuke.math.Matrix4()
                pmFrom = nuke.math.Matrix4()
                    
                imageWidth = float(cp.width())
                imageHeight = float(cp.height())
                    
                to1x = cp['to1'].getValueAt(i)[0]
                to1y = cp['to1'].getValueAt(i)[1]
                to2x = cp['to2'].getValueAt(i)[0]
                to2y = cp['to2'].getValueAt(i)[1]
                to3x = cp['to3'].getValueAt(i)[0]
                to3y = cp['to3'].getValueAt(i)[1]
                to4x = cp['to4'].getValueAt(i)[0]
                to4y = cp['to4'].getValueAt(i)[1]
                    
                from1x = cp['from1'].getValueAt(i)[0]
                from1y = cp['from1'].getValueAt(i)[1]
                from2x = cp['from2'].getValueAt(i)[0]
                from2y = cp['from2'].getValueAt(i)[1]
                from3x = cp['from3'].getValueAt(i)[0]
                from3y = cp['from3'].getValueAt(i)[1]
                from4x = cp['from4'].getValueAt(i)[0]
                from4y = cp['from4'].getValueAt(i)[1]
                    
                    
                pmTo.mapUnitSquareToQuad(to1x,to1y,to2x,to2y,to3x,to3y,to4x,to4y)
                pmFrom.mapUnitSquareToQuad(from1x,from1y,from2x,from2y,from3x,from3y,from4x,from4y)
                    
                mtx = pmTo*pmFrom.inverse()    
                mtx.transpose()
                    
                return mtx
                
            #---------------------------------------------------------------------------------------
            
 
 
            #--------------------------------''' Define Frame Range'''---------------------------------    
    
            frames = nuke.getFramesAndViews('get FrameRange', '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
            frame_range = nuke.FrameRange( frames[0] ) 
              
            #---------------------------------------------------------------------------------------  
                    
            for i in frame_range:
 

                mtx = getAnimatedCPasMTX(input, i)
                              
                #------------------------------------------------------------------------------
                #apply values
                
                targetKnob.setAnimated()
                for j in range(16):
                    targetKnob.setValueAt(mtx[j], i, j )
                                                       
                                   
                #-----------------------------------------------------------------------------------------------    
            
 
        
        else:
    
            nuke.message('please select a CPin node')
     
     
#end script





def cpToMatrixMenu() :
    n = nuke.selectedNodes()

    try: 
        nuke.selectedNode()
    except:
        print nuke.message("Select a CornerPin2D and a Roto or Rotopaint!")

    for nodes in n:
        if nodes.Class() != 'RotoPaint' and nodes.Class() != 'Roto' and nodes.Class() != 'CornerPin2D':
            nuke.message("Select a Tracker and a Roto or Rotopaint!")
            break
        elif len(n) == 1:
			if nodes.Class() == 'CornerPin2D' :
				p = nuke.createNode('CornerPin2D')
			else:
				nuke.message("Select a CornerPin2D and a Roto or Rotopaint!")

    for node in n:
        if node.Class() == 'RotoPaint' or node.Class() == 'Roto' :
            p = node
        elif node.Class() == 'CornerPin2D':
            track = node
            if track['label'].value() :
                tName = track['label'].value()
            else:
                tName = track['name'].value()
                
                
    cpToMatrix(p,track)
     
def cpToMatrixInNode():
    n=nuke.selectedNode()
    if n.Class()=='CornerPin2D':
        cpToMatrix(nuke.thisNode(),n)
    else:
        nuke.message('please select a cornerPin node')

def stablizeFromRotoLayer(rotoNode):
    r=rotoNode
    if r.Class() == 'RotoPaint' or r.Class() == 'Roto':
        cp=nuke.createNode('CornerPin2D')
        cp['invert'].setValue(True)
        cp['label'].setValue('TempStablize')
        cp['transform_matrix'].fromScript(r['transform_matrix'].toScript())

def dieBefore():
    n=nuke.thisNode()
    F=nuke.frame()
    e=n['lifetime_end'].getValue()
    n['lifetime_type'].setValue(4)
    n['lifetime_start'].setValue(F)
    n['lifetime_end'].setValue(e)
def singleFrame():
    n=nuke.thisNode()
    F=nuke.frame()
    n['lifetime_type'].setValue(2)
    k=n['lifetime_start'].setValue(F)
    k=n['lifetime_end'].setValue(F)
def dieAfter():
    n=nuke.thisNode()
    F=nuke.frame()
    s=n['lifetime_start'].getValue()
    n['lifetime_type'].setValue(4)
    n['lifetime_end'].setValue(F)
    n['lifetime_start'].setValue(s)



def addMoTab():
    newTab=nuke.Tab_Knob('Mo_tab') 
    cpToMatrixKnob=nuke.PyScript_Knob("CornerPinToMatrix",'CornerPin To Matrix','from Mo_RotoTools import cpToMatrixInNode\ncpToMatrixInNode()')
    cpToMatrixKnob.setFlag(nuke.STARTLINE)
    stablizeKnob=nuke.PyScript_Knob("stablizeFromRotoLayer",'Stablize From Roto Layer','from Mo_RotoTools import stablizeFromRotoLayer\nstablizeFromRotoLayer(nuke.thisNode())')
    dieBeforeKnob=nuke.PyScript_Knob("dieBefore",'Die Before','from Mo_RotoTools import dieBefore\ndieBefore()')
    singleFrameKnob=nuke.PyScript_Knob("singleFrame",'Single Frame','from Mo_RotoTools import singleFrame\nsingleFrame()')
    dieAfterKnob=nuke.PyScript_Knob("dieAfter",'Die After','from Mo_RotoTools import dieAfter\ndieAfter()')
    tracking=nuke.Text_Knob('tracking','Tracking')
    LifeTime=nuke.Text_Knob('lifetime','Life Time')
    fromValueKnob=nuke.Int_Knob('fromValue','From')
    toValueKnob=nuke.Int_Knob('toValue','To')
    toValueKnob.clearFlag(nuke.STARTLINE)

    node=nuke.thisNode()
    node.addKnob(newTab)
    node.addKnob(LifeTime)
    node.addKnob(dieBeforeKnob)
    node.addKnob(singleFrameKnob)
    node.addKnob(dieAfterKnob)
    node.addKnob(fromValueKnob)
    node.addKnob(toValueKnob)
    node.addKnob(tracking)
    node.addKnob(cpToMatrixKnob)
    node.addKnob(stablizeKnob)
    node.knob('fromValue').setExpression('lifetime_start')
    node.knob('toValue').setExpression('lifetime_end')
    
    
    
    
    

           
           
           
           
           
           
    
    
     





