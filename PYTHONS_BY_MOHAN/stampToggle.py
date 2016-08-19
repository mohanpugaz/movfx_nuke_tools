#### code snippet by MOHAN_PUGAZ
#### POSTAGE STAMP TOGGLE


def stampToggle():
    
    sel = nuke.selectedNodes()
    if sel:
        for n in sel:
            
            m=n['postage_stamp'].getValue()
          
            if m==0.0:
                n['postage_stamp'].setValue(1)
            if m==1.0:
                n['postage_stamp'].setValue(0)
    else:
        nuke.message('Select Nodes to toggle postage Stamps')

