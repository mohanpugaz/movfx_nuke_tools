
import nuke
import os

frame = nuke.frame()
sel = nuke.selectedNode()
readFF = int(sel['first'].getValue())
readLF = int(sel['last'].getValue())

selPath = sel['file'].getValue()
path = os.path.dirname(selPath)
file = os.path.basename(selPath)
fileName = os.path.splitext(file)[0]

nodeFormat = sel.format()
format = nodeFormat.name()

###Adding neccesary formats
thumbnail = '80 80 thumbnail'
prevImg = '590 300 prevImg'
tempHD = '1080 720 tempHD'

nuke.addFormat( thumbnail )
nuke.addFormat( prevImg )
nuke.addFormat( tempHD )

###setup for thumbnail

tRef=nuke.createNode('Reformat')
tRef['black_outside'].setValue( True )
tRef['format'].setValue( 'thumbnail' )

thumbFile=path+'/'+fileName+r"_thumbnail.jpg"
tWrite = nuke.createNode( 'Write' )
tWrite['file'].setValue(thumbFile)

nuke.execute(tWrite , frame , frame)

nuke.delete(tWrite)
nuke.delete(tRef)
nukescripts.clear_selection_recursive()

###setup for prevImg
sel['selected'].setValue( True )

pRef=nuke.createNode('Reformat')
pRef['black_outside'].setValue( True )
pRef['format'].setValue( 'prevImg' )

prevImgFile=path+'/'+fileName+r"_prevImg.jpg"
pWrite = nuke.createNode( 'Write' )
pWrite['file'].setValue(prevImgFile)

nuke.execute(pWrite , frame , frame)

nuke.delete(pWrite)
nuke.delete(pRef) 
nukescripts.clear_selection_recursive()

###setup for prevVid
sel['selected'].setValue( True )

pvRef=nuke.createNode('Reformat')
pvRef['black_outside'].setValue( True )
pvRef['format'].setValue( 'tempHD' )

prevVidFile=path+'/'+fileName+r"_prev.mp4"
pvWrite = nuke.createNode( 'Write' )
pvWrite['file'].setValue(prevVidFile)
pvWrite['file_type'].setValue( 'mov' )

nuke.execute(pvWrite , readFF , readLF)

nuke.delete(pvWrite)
nuke.delete(pvRef)
