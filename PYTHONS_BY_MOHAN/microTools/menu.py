import nuke
from microTools import copyPremult 

menu = nuke.menu('Nuke')
mMenu = menu.addMenu("Mo_Tools/MicroTools",icon="M.jpg")

mMenu.addCommand("Copy and Premult" , lambda:copyPremult() , "++k" , icon = "M.jpg" )
