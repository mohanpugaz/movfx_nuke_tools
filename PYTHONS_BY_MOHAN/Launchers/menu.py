from Launchers import openMochaPro,openSil,openMpcMail,openSyncIt

menu=nuke.menu('Nuke')
launchersMenu=menu.addMenu('Mo_Tools/Launchers',icon="M.jpg")

launchersMenu.addCommand('Mail',lambda:openMpcMail(),icon="mail.tif")
launchersMenu.addCommand('MochaPro',lambda:openMochaPro(),icon="mochaproicon.png")
launchersMenu.addCommand('Sillhoutte Fx',lambda:openSil(),icon="sil_icon.png")
launchersMenu.addCommand('SyncIt',lambda:openSyncIt(),icon="syncIt.tif")




Mn_Toolbar=nuke.toolbar("Mo Nodes")
launcher=Mn_Toolbar.addMenu("Launchers",icon="launcher.png")

launcher.addCommand("Open Sillhoutte",lambda:openSil(),icon="sil_icon.png")
launcher.addCommand("Open Mocha",lambda:openMocha(),icon="mochaproicon.png")
launcher.addCommand("Open SyncIt",lambda:openSyncIt(),icon="syncIt.tif")
launcher.addCommand("Mpc Mail",lambda:openMpcMail(),icon="mail.tif")
