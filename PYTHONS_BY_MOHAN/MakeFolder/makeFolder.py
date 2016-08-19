#-------------------------------------------------------------------------------
# Name		:makeFolder
# Purpose	:Creates the given directory in the write node if it does not exists and render
#
# Author	:Mohan Pugaz
#
# Created	:25-06-2015
# Copyright	:(c) mohanpugaz 2015
# 
#-------------------------------------------------------------------------------


#for menu.py (without #)
#
#from makeFolder import makeFolder
#nuke.addBeforeRender(makeFolder,nodeClass='Write')   
#


import os
import nuke
import webbrowser as wb

def makeFolder():
    node=nuke.thisNode()
    dirPath=node['file'].getValue()
    dirPath=os.path.dirname(dirPath)
    print dirPath


    if os.path.isdir(dirPath):
        print 'Path exist'
    else:
        print 'Path not exist'
        q=nuke.ask(r"Folder does not exists,do you want to create that?"+dirPath)
        print q
    
        if q==True:
           
            os.makedirs(dirPath)
            wb.open(dirPath)
            print 'Directory created'
        else:
            pass
    
    return dirPath
    
    
    
    
