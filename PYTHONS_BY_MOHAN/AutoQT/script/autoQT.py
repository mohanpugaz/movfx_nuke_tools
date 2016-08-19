####___CREATED ON 10.05.2015 BY MOHAN PUGAZ , AN INDIAN COMPOSITOR!___
####___feel free to give any sugestions.. mohanpugaz@gmail.com
### Use at your own risk

#1.Just select the readnodes you want to render 
#2.Run the script
#3.set the output path 
#4.And watch every files are ready to render an mov.
####

#### 
#1.This code will automatically sets the frame range for you from the read node on its upstream
#2.Automatically takes the filename from the corresponding read node


#for menu
#from autoQT import AutoQT
#men=nuke.menu('Nuke')
#men.addCommand('M_TOOLS/AutoQT',lambda:AutoQT(),'shift+q')
#

import os
import nuke

def AutoQT():
    pan=nuke.Panel('AutoQT_by_ mohanpugaz@gmail.com')
    pan.addFilenameSearch('OUT PATH','output path here')
    pan.addEnumerationPulldown('Select Size','PAL HD 1K_Super_35(full-ap)')
    pan.show()
    
    
    Output_Path=pan.value('OUT PATH')
    QT_Size=pan.value('Select Size')
    
    
    sel=nuke.selectedNodes()
    
    
    for m in sel:
    
        fn=nuke.filename(m)
        fn=os.path.basename(fn)
        fn=os.path.splitext(fn)[0]
        firstFrame=m.knob('first').getValue()
        lastFrame=m.knob('last').getValue()
        print fn
        
    
        rf=nuke.createNode("Reformat")
        rf.setInput(0,m)
        rf['format'].setValue(QT_Size)
        rf['black_outside'].setValue('True')
    
    
        wr=nuke.createNode("Write")
        wr.setInput(0,rf)
        wr['file'].setValue(Output_Path+fn+".mov")
        wr['file_type'].setValue('mov')
        wr['codec'].setValue('none')
        wr['use_limit'].setValue('True')
        wr['first'].setValue(firstFrame)
        wr['last'].setValue(lastFrame)
    return()
    



