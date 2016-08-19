
import nuke
import os
import webbrowser as wb


def openScriptFolder():
    
    wf=nuke.scriptName()
    dir=os.path.dirname(wf)
    wb.open(dir)

    return 
