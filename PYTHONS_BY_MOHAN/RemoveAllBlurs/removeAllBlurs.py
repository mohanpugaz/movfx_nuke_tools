######
'''WIP'''
#####



import nuke.rotopaint as rp,nukescripts, nuke

rp_node = nuke.selectedNode()
elements = {}

def parse_layer(layer, elements, parents):
    """Return a list of all Shapes or Strokes in a Roto or Rotopaint node's heirarchy, with a list of all parent Layers for each item."""
    for e in layer:
        if isinstance(e, rp.Shape):
            elements['Shapes'].append([e, parents])
        elif isinstance(e, rp.Stroke):
            elements['Strokes'].append([e, parents])
        elif isinstance(e, rp.Layer):
            parents_copy = parents[:]
            parents_copy.insert(0, e)
            elements = parse_layer(e, elements, parents_copy)
    return elements

def get_elements():
    """    Get all Shape Stroke and Layer elements in our Roto/Paint node."""
    elements = { 'Shapes':[], 'Strokes':[] }
    curves_knob = rp_node['curves']
    root_layer = curves_knob.rootLayer
    elements = parse_layer(root_layer, elements, [root_layer])
    print elements


get_elements()
