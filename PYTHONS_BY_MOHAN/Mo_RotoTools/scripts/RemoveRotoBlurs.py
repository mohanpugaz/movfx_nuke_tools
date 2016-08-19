import nuke.rotopaint as rp,nukescripts, nuke


def parse_layer(layer, elements, parents):
    """Return a list of all Shapes and Layers."""
    for e in layer:
        if isinstance(e, rp.Shape):
            elements['Shapes'].append(e)
        elif isinstance(e, rp.Layer):
            parents_copy = parents[:]
            parents_copy.insert(0, e)
            elements['Layers'].append(e)
            elements = parse_layer(e, elements, parents_copy)
    return elements

def get_elements(node):
    """    Get all Shape Stroke and Layer elements in our Roto/Paint node."""
    rp_node = node
    shapeList = []
    layersList = []
    elements = { 'Shapes':[], 'Layers':[] }
    curves_knob = rp_node['curves']
    root_layer = curves_knob.rootLayer
    elements = parse_layer(root_layer, elements, [root_layer])
    shapeList = elements['Shapes']
    layerList = elements['Layers']
    elements = shapeList+layerList
    return elements

def removeBlurs(node):
    rp_node = node
    curveKnob=rp_node['curves']
    root=curveKnob.rootLayer
    
    allElements=get_elements(rp_node)   
    allElements.append(root) 
    for element in allElements:
        print element.name
        atts=element.getAttributes()
        atts.set('fo',False)
        atts.set('mbo',False)


        
    
