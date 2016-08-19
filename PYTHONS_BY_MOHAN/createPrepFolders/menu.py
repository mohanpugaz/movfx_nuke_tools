from createPrepFolders import createPrepFolders


Mn_Toolbar=nuke.toolbar("Mo Nodes")
Mn_Toolbar.addCommand('Create_Folder/Create_Prep_Folders',lambda:createPrepFolders(),icon="add_folder.png")

n=nuke.menu('Nuke')
n.addCommand('Mo_Tools/Create_Folder/Create_Prep_Folders',lambda:createPrepFolders(),icon="add_folder.png")
