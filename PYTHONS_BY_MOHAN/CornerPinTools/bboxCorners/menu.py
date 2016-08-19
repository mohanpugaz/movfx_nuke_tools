import nuke
from bboxCorners import bboxCorners

m=nuke.menu('Nuke')
m.addCommand('Mo_Tools/CornerPinTools/Set Corners To BBox',lambda:bboxCorners(nuke.createNode('CornerPin2D')) , icon="M.jpg")
