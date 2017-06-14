"""
Description : This tool will collect all the paths of the read nodes,
              write nodes,etc on the nuke script based on the users selection 
              and give it out in a pop up window
Author      : mohan-p (mohanpugaz@gmail.com)

Usage       : Just run it on your final comp scene!

"""

import nuke
import os

def getPath(nodes):
    paths = []
    for node in nodes:
        file = node['file'].getValue()
        filePath = os.path.dirname(file)
        paths.append(filePath)
    return paths

def getElements():
    reads = []
    writes = []
    cameras = []
    readGeos = []
    writeGeos = []
    
    nodes = nuke.selectedNodes()
    
    if nodes:
        nodes = nodes
    else:
        nodes = nuke.allNodes()
        
    for n in nodes:
        if n.Class()=='Read':
            reads.append(n)
        if n.Class()=='Write':
            writes.append(n)
        if n.Class()=='Camera2':
            cameras.append(n)
        if n.Class()=='ReadGeo':
            readGeos.append(n)
        if n.Class()=="WriteGeo":
            writeGeos.append(n)
    
    p = nuke.Panel("P")
    p.addBooleanCheckBox("reads",True)
    p.addBooleanCheckBox("writes",True)
    p.addBooleanCheckBox("readGeos",False)
    p.addBooleanCheckBox("writeGeos",False)
    p.addBooleanCheckBox("cameras",False)
    p.show()
    
    pathList = []
    readsPath = []
    writesPath = []
    readGeosPath = []
    writeGeosPath = []
    camerasPath = []
    
    if p.value('reads') == 1:
        readsPath = getPath(reads)
    else:
        pass    
    if p.value('writes') == 1:
        writesPath = getPath(writes)
    else:
        pass    
    if p.value('readGeos') == 1:
        readGeosPath = getPath(readGeos)
    else:
        pass    
    if p.value('writeGeos') == 1:
        writeGeosPath = getPath(writeGeos)
    else:
        pass
    if p.value('cameras') == 1:
        camerasPath = getPath(cameras)
    else:
        pass
    
    pathList = readsPath + writesPath + readGeosPath + writeGeosPath + camerasPath
    
    outPaths = ""
    for path in pathList:
        outPaths = outPaths +"\n" + path
    return nuke.message(outPaths)
