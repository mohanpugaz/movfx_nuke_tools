# THE MATTE ENGINE
# AUTHOR - MOHAN PUGAZ an INDIAN COMPOSITOR
# CREATED ON 12-05-2015
# mail me ___ mohanpugaz@gmail.com
# Im Waiting for my dream job , if you are interested in my works and can help me please contact me.
# Mobile : +91 9176478150

###for menu.py 
#from matteEngine import matteEngine
#menu=nuke.menu('Nuke')
#menu.addCommand('M_TOOLS/MatteEngine',lambda:matteEngine())

import nuke
 
def matteEngine():
    sel=nuke.selectedNode()
    moPanel=nuke.Panel('Matte Engine____BY MOHAN PUGAZ')
    
    moPanel.addBooleanCheckBox('RED', '')
    moPanel.addBooleanCheckBox('GREEN', '')
    moPanel.addBooleanCheckBox('BLUE', '')
    moPanel.addBooleanCheckBox('CYAN', '')
    moPanel.addBooleanCheckBox('MAGENTA', '')
    moPanel.addBooleanCheckBox('YELLOW', '')
    moPanel.addBooleanCheckBox('PURE WHITE', '')
    moPanel.addBooleanCheckBox('PURE BLACK', '')
    moPanel.addBooleanCheckBox('ALPHA 0', '')
    moPanel.addBooleanCheckBox('ALPHA 1', '')
    moPanel.addSingleLineInput('Custom Expression','')
    moPanel.show()
    
    redmatte=moPanel.value('RED')
    greenmatte=moPanel.value('GREEN')
    bluematte=moPanel.value('BLUE')
    cyanmatte=moPanel.value('CYAN')
    magentamatte=moPanel.value('MAGENTA')
    yellowmatte=moPanel.value('YELLOW')
    whitematte=moPanel.value('PURE WHITE')
    blackmatte=moPanel.value('PURE BLACK')
    alphaInvert=moPanel.value('ALPHA 0')
    alpha=moPanel.value('ALPHA 1')
    
    
    redExpr=('clamp(r-(b+g))')
    greenExpr=('clamp(g-(b+r))')
    blueExpr=('clamp(b-(g+r))')
    magExpr=('clamp(r*b-g)')
    yellowExpr=('clamp(r*g-b)')
    cyanExpr=('clamp(b*g-r)')
    whiteExpr=('r*g*b')
    blackExpr=('(r+g+b)==0')
    alphaExpr=('clamp(a)')
    alphaInvExpr=('1-clamp(a)')
    customExpr=moPanel.value('Custom Expression')
    
   

    def setAttrs(r,g,b,expr):
    
        Node=nuke.createNode('Expression')
        
        
       
        
        hexColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16)
        
        Node.setInput(0,sel)
      
        Node['tile_color'].setValue(hexColour)
        Node['expr0'].setValue('0')
        Node['expr1'].setValue('0')
        Node['expr2'].setValue('0')
        Node['expr3'].setValue(expr)
        return
    
    if redmatte is True:
        setAttrs(1,0,0,redExpr)
        pass
    if greenmatte is True:
        setAttrs(0,1,0,greenExpr)
        pass
    if bluematte is True:
        setAttrs(0,0,1,blueExpr)
        pass
    if magentamatte is True:
        setAttrs(1,0,1,magExpr)
        pass
    if yellowmatte is True:
        setAttrs(1,1,0,yellowExpr)
        pass
    if cyanmatte is True:
        setAttrs(0,1,1,cyanExpr)
        pass
    if whitematte is True:
        setAttrs(1,1,1,whiteExpr)
        pass
    if blackmatte is True:
        setAttrs(0,0,0,blackExpr)
        pass
    if alpha is True:
        setAttrs(1,1,1,alphaExpr)
        pass
    if alphaInvert is True:
        setAttrs(1,1,1,alphaInvExpr)
        pass
    
    if customExpr:
        setAttrs(1,1,1,customExpr)
     
    
    return

   

