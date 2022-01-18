# -*- coding: utf-8 -*-
"""
Camera 

Class for a generic discreet pixel sensor rectangular array camera.
Most often implemented by a CCD or CMOS chip.
 
Constructor:
    Camera (name, pixSize, width, height)
        name    :: descriptive string for this camera
        pixSize :: physical sensor square pixel size in µm
        width   :: number of pixels in horizontal (U) direction
        height  :: number of pixels in vertical (V) direction
 
Methods:
    sensorSize
    print
    
Future fields that might belong here:
    Bayer mask (or other/none)
    Spectral response function (transmittance versus wavelength, per channel)

"""

import numpy as np

class Camera ():
    def __init__(self, name, pixSize, width, height):
        self.name      = name;
        self.pixWidth  = pixSize;   # square pixels are very common
        self.pixHeight = pixSize;   # square pixels are very very common
        self.imWidth   = width;
        self.imHeight  = height;
        return
        
    def sensorSize (self):
        # Return the nominal sensor size in inches.  This is a fuzzy
        # concept, based on historical standard sizes like 1/2, 1/3,
        # 1/1.8 inches, etc.  The nominal sensor size is larger than
        # an actual modern semiconductor sensor by a factor of about
        # 3/2. This function clamps to various common sizes.  The
        # result should not be used for any quantitative calculation.
        # See, for example
        # http://www.dpreview.com/news/0210/02100402sensorsizes.asp
        diag = self.sensorDiag ();
        ssize = (diag * (3/2)) / 25.4;
        commonValues = [ 1/4, 1/3, 1/2, 1/1.8, 2/3, 1];
        sensorSize = commonValues[np.abs(np.array(ssize) - commonValues).argmin()] # closestValue (ssize, commonValues);
        return sensorSize
        
    def print (self, level=0):
        indentation = np.repmat (' ' *4*level);

        print (indentation + 'Camera: {self.name}:\n')
        print (indentation + '    Pixel size = {self.pixWidth}x{self.pixHeight} µm\n')
        print (indentation + '    Image size = {self.imWidth}x{self.imHeight} pixels\n')
        print (indentation + '    Nominal sensor size = {self.sensorSize:2.4} inch\n')
        print (indentation + '    Actual sensor diagonal = {self.sensorDiag:2.4} mm\n')
        return
    
    def sensorDiag (self):
        #Return the diagonal sensor size in mm
        sensorDiag = np.hypot (self.imWidth*self.pixWidth, self.imHeight*self.pixHeight) / 1000;
        return sensorDiag 

