import nuke

root=nuke.root()
size=root.format().r()

frame=nuke.frame()
nframe=frame+1
pframe=frame-1
sel=nuke.selectedNode()
cKnob=sel['curves']
selShapes=cKnob.getSelected()

def break(direction):
	for s in selShapes:
	    A=s.getAttributes()
	    A.set(frame,'opc',0)
	    if direction==forward:
			A.set(pframe,'opc',1)
		if direction==backward:
	    	A.set(nframe,'opc',1)

	    T=s.getTransform()
	    T.addTranslationKey(frame,0,0,0)
	    T.addTranslationKey(pframe,size,0,0)
	return


'''
def breakB():
	for s in selShapes:
	    A=s.getAttributes()
	    A.set(frame,'opc',0)
	    A.set(nframe,'opc',1)
	    
	    T=s.getTransform()
	    T.addTranslationKey(frame,0,0,0)
	    T.addTranslationKey(pframe,size,0,0)
	return

def breakF():
	for s in selShapes:
	    A=s.getAttributes()
	    A.set(frame,'opc',0)
		A.set(pframe,'opc',1)
	    
	    T=s.getTransform()
	    T.addTranslationKey(frame,0,0,0)
	    T.addTranslationKey(nframe,size,0,0)
	return
'''
