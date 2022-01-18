# -*- coding: utf-8 -*-
"""
CameraLens

Class for a combined camera (sensor) and lens.
 
Constructor:
    CameraLens (camera, lens)
        camera      :: reference to a camera object
        lens        :: reference to a lens object
 
Methods:
    width   : return the image width
    height  : return the image height
    hfov    : return the horizontal field of view in degrees
    vfov    : return the vertical field of view in degrees
    print   : pretty-print the camera/lens parameters

"""

from indent import indent
import numpy as np

class CameraLens(): 
    def __init__ (self, camera, lens):
        self.camera = camera;
        self.lens = lens;
        
        if lens.maxSensorSize < camera.sensorSize():
            return
        return
    
    def width (self):
        width = self.camera.imWidth;
        return width
        
    def height (self):
        height = self.camera.imHeight;
        return height
        
    def hfov (self):
        d = (self.camera.pixWidth * self.camera.imWidth) / 1000;
        hfov = 2 * np.degrees(np.arctan (d / (2*self.lens.focalLength)));
        return hfov
        
    def vfov (self):
        d = (self.camera.pixHeight * self.camera.imHeight) / 1000;
        vfov = 2 * np.degrees(np.arctan (d / (2*self.lens.focalLength)));
        return vfov 
        
    def print (self, level=0, depth=0):
        degree_sign = u'\N{DEGREE SIGN}'
        print (indent(level) + f'{self.camera.name} with {self.lens.name}')
        print (indent(level+1) + f'Fields of view = {self.hfov():.2f}{degree_sign}H {self.vfov():.2f}{degree_sign}V\n');
        
        if depth > 0:
            self.camera.print (level+1, depth-1);
            self.lens.print (level+1, depth-1);
