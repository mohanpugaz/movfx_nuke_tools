import nuke,sys,os
import webbrowser as wb


def launch(directory):
    # Open folder
    print('Attempting to open folder: ' + directory)
    if os.path.exists( directory ):
        if(sys.platform == 'win32'):
            os.system('start ' + directory)
        elif(sys.platform == 'darwin'):
            os.system('open ' + directory)
    else:
        nuke.message('Path does not exist:\n' + directory)


def openReadnode():

    error = False

    try:
        sel=nuke.selectedNode()
        selectedNodeFilePath=sel.knob('file').getValue()
        selectedNodeFilePath=os.path.dirname(selectedNodeFilePath)
     

    except ValueError:
        error = True
        nuke.message('No node selected.')
    except NameError:
        error = True
        nuke.message('You must select a Read node or a Write node.')

    if error == False:
        print('Directory: ' +selectedNodeFilePath)
     
        wb.open(selectedNodeFilePath)





