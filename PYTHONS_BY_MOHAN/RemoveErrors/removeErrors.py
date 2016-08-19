###PYTHON SNIPPET BY MOHAN_PUGAZ
###DELETE ERRORS


import nuke

def removeErrors():
    for a in nuke.allNodes('Read'):
        if a.error() == True:
            nuke.delete(a)
        else:
            pass
    

