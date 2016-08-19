######
'''WIP'''
#####


import nuke.rotopaint as rp

rotoNode=nuke.selectedNode()
curveKnob=rotoNode['curves']
root=curveKnob.rootLayer

att=root.getAttributes()
att.set('fo',False)
att.set('mbo',False)

for element in root:
    if isinstance(element, rp.Layer):
        layerLevelOne=element
        for l in layerLevelOne:
            if isinstance(l, rp.Layer):
                layerLevelTwo=l
                for ll in layerLevelTwo:
                    if isinstance(ll, rp.Layer):
                        layerLevelThree=ll
                        print layerLevelThree.name

layers=[layerLevelOne,layerLevelTwo,layerLevelThree]

for layer in layers:
    atts=layer.getAttributes()
    atts.set('fo',False)
    atts.set('mbo',False)
