############################
#
#Assign - By Mohanpugaz
#mohan-p@gmail.com
#
#############################
#INSTALLATION
#____________
#copy this file to your custom nuke python directory or nuke home directory
#copy and paste these two lines on menu.py(without ' # ' )
#
#nuke.addOnUserCreate(addAssign,nodeClass=('Read'))
#menu=nuke.menu('Nuke')
#menu.addCommand('Mo_Tools/assign',lambda:main())
#
##############################
#USAGE:
#____________
#On each read nodes new tab called assign is added 
#On the assign tab u can enter the artist name and mandays 
#select the shots to be assigned and then click on the assign button(hotkey 'alt+a')
#then it will give you the list of shots with corresponding artist and mandays for the shot.
#you can copy paste and send the mail to the artists
#
###############################
import nuke

#Adding custom knobs to the read  nodes to get the input from user
def addAssign(node):
    
    file=node['file'].getValue()
    
    assignTab=nuke.Tab_Knob('assign')
    fileKnob=nuke.Text_Knob('filePath',file)
    artistKnob=nuke.EvalString_Knob('artistName','Artist Name','-')
    mandaysKnob=nuke.EvalString_Knob('mandays','Mandays','1')
    
    
    node.addKnob(assignTab)
    
    node.addKnob(artistKnob)
    node.addKnob(mandaysKnob)
    return 

def addAssignManual():
    nodes=nuke.selectedNodes()
    for n in nodes:
        addAssign(n)
    
def addAssignAuto():
    node=nuke.thisNode()
    addAssign(node)


#Collecting the user inputs from assign tab which is created above
def getInfos(nodes):
    dictShot={}
    shotList=[]
    for node in nodes:
        shot=node['file'].getValue()
        artist=node['artistName'].evaluate()
        mandays=node['mandays'].evaluate()
        dictShot={'shot':shot , 'artist': artist , 'mandays':mandays}
        shotStr=dictShot['shot']+'    -'+dictShot['mandays']+'-'+dictShot['artist']      
        shotList.append(shotStr)
    return shotList    


#making the shot list and disply it for the user to copy the collected infos
def main():
    sel=nuke.selectedNodes()
    n=[]
    for node in sel:
        if node.Class()=='Read':
            n.append(node)
        else:
            nuke.message('please select a read node')
            break
    
    for node in n:
        if node['mandays'].getValue()==0.0:
            nuke.message('please fill all mandays')
        elif node['artistName'].getValue()==0.0:
            nuke.message('please fill all artistNames')
        
    if n:
        list=getInfos(n)
        list='\n'.join(list)
        message=nuke.message(list)
    else:
        message=nuke.message('no nodes selected')
    print "Assign - by Mohan pugaz"
    return message
    
    
    
def getFilePaths():
    
    sel=nuke.selectedNodes()   
    shotList=[]
    if sel:
        for n in sel:
            f=n['file'].getValue()
            shotList.append(f)

        shotList='\n'.join(shotList)
        message=nuke.message(shotList)
    else:
        message=nuke.message('Please select read nodes')
    return message
