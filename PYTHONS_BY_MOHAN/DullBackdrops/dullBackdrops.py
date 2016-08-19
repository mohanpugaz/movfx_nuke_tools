import nuke
import random

def dullColor():
    r = (float(random.randint( 20, 25)))/100
    g = (float(random.randint( 20, 25)))/100
    b = (float(random.randint( 20, 25)))/100
    dullColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16)
    return dullColor

