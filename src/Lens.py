# -*- coding: utf-8 -*-
"""
Lens 

Class for a generic lens.
 
Constructor:
    Lens (name, focalLength, maxSensorSize)
        name            :: descriptive string
        focalLength     :: stated (effictive) focal length of the lens in mm
        maxSensorSize   :: maximun nominal (diagonal) sensor size in inches
 
Methods:
    print   : pretty-print the lens parameters

"""

import numpy as np

class Lens ():
    def __init__ (self, name, focalLength, maxSensorSize):
        self.name = name
        self.focalLength = focalLength
        self.maxSensorSize = maxSensorSize
        return
        
    def print (self, level=0):
        indentation = np.repmat (' ', 1, 4*level);

        print (indentation + 'Lens: {self.name}:\n')
        print (indentation + '    Focal length = {self.focalLength} mm\n')
        print (indentation + '    Maximum sensor size = {self.maxSensorSize} inch\n')
        return
