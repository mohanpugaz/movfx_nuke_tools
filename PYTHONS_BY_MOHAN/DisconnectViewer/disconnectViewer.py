import nuke
def disconnectViewer():
    
    n=[0,1,2,3,4,5,6,7,8,9,10]
    nodes=nuke.allNodes()
    for i in nodes:
        cls=i.Class()
        if cls=='Viewer':
            print cls
            for nums in n:
                i.setInput(nums,None)
    return 'disconnected'

