##___SAVEREF__##

##Created By Mohan Pugaz
##for bugs and reports please mail me mohan-p@moving-picture.com

##DESCRIPTION
#I created this to easily save a refference image for roto in nuke
#Just drop a rotopaint node under the input and draw the refference or add a text and run the script
#It will render whatever is visible in that particular frame you are viewing in the folder where the input lives

##-INSTALLATION
#1-copy the saveRef folder to wherever you want
#2-find "init.py" inside the ".nuke" folder in your home directory
#3-Add this line to the init.py file(without double quotes) "nuke.pluginAddPath('YOUR PATH/saveRef')"
#4-If you can't find init.py file in ".nuke" folder you can just create one

##-USAGE
#To run the script you can go to Mo_Tools in menubar and click on saveRef or
#just press alt+shift+r or ofcourse you can modify the shortcut and menus in menu.py file provided.  




import nuke
import nukescripts
import os


def find_upstream_node( matchclass=None, startnode=None ):
    """
    In the simplest way possible, this function will go upstream and find
    the first node matching the specified class.
    """

    if matchclass == None:
        return None
    #
    if startnode == None:
        return None
    #
    if  startnode.Class() == matchclass:
        return startnode
    else:
        return find_upstream_node( matchclass=matchclass, startnode=startnode.input( 0 ) )


def saveRef ():
    
    f=find_upstream_node( 'Read', nuke.selectedNode())
    file=f['file'].getValue()
    path=os.path.dirname(file)
    
    filename=os.path.basename(file)
    filename=os.path.splitext(filename)[0]
    ### getting active node
    curViewer = nuke.activeViewer()
    curNode = curViewer.node()
    acticeVinput = curViewer.activeInput()
    curN = curNode.input(acticeVinput)

    ###create a reformat
    nuke.addFormat('1920 1080 tHD')
    
    re=nuke.createNode("Reformat")
    re.setName("tempReformat")
    re['format'].setValue('tHD')
    re['black_outside'].setValue(1)
    re.setInput(0, curN)
    
    ### creating temp write
    path=path+'/'+filename+'_'+'ref.jpg'
    w = nuke.createNode("Write")
    w.setName("tempWrite")
    w.setInput(0, re)
    w['file'].setValue(path)
    w['file_type'].setValue('jpeg')


    ### setting current frame for render
    result = nuke.frame()
    if result =="":
      result = result

    ### execute write node
    nuke.execute(w, (int(result)), result)
    name = w.knob('file').value()
    nukescripts.node_delete(popupOnError=True)
    nuke.delete(re)

    
    if fileType == "":
        return
