#Created by Mohan Pugaz
import os
import nuke
from mpc import jobtools as _jobtools


def createPrepFolders():
    user=os.getenv('USER')
    job=os.getenv('JOB')
    shot=os.getenv('SHOT')
    panel=nuke.Panel('Create Prep folder structure - by Mohan pugaz')
    panel.addSingleLineInput('artist',user)
    
    if shot == None:
        panel.addFilenameSearch('path','/jobs/'+job+'/')
    if shot:
        panel.addFilenameSearch('path','/jobs/'+job+'/'+shot+'/nuke/comp/scene/')

    
    if not panel.show():
        return
    
    artist=panel.value('artist')
    path=panel.value('path')

    os.mkdir(path+artist)
    os.mkdir(path+artist+'/'+'mocha')
    os.mkdir(path+artist+'/'+'shapes')
    
    
    shotname=os.getenv('SHOTNAME')
    if shot:
        nuke.scriptSaveAs(path+artist+'/'+'F_%s_cleanUp_v001.nk' %shotname , -1)
    if shot == None:
        nuke.scriptSaveAs(path+artist+'/'+'F_CleanUp_v001.nk', -1)
        
    return artist
