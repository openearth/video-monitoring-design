# -*- coding: utf-8 -*-
"""
MountedCamera

Class for a specific, mounted camera and lens
 
Constructor:
    MountedCamera (name, location, azimuth, tilt, roll, camera, lens)
        name        :: descriptive string
        location	:: reference to a Location object
        azimuth     :: azimuth in degrees (compass orientation)
        tilt        :: tilt in degrees (horizontal 0 to downward 90)
        roll        :: camera roll about prinicple axis
        camlens     :: reference to a CameraLens object
 
Methods:
    print   : pretty-print the parameters

"""

from CameraFootprint import CameraFootprint
from indent import indent

class MountedCamera():

    def __init__ (self, name, location, azimuth, tilt, roll, camlens):
        self.name      = name;
        self.location  = location;
        self.azimuth   = azimuth;
        self.tilt      = tilt;
        self.roll      = roll;
        self.camlens   = camlens;
        self.footprint = CameraFootprint (self);
        return
        
    def printing (self, level=0):
        
        print (indent(level) + f'VideoCamera: {self.name[0]}:');
        self.location.print (level+1);
        print (indent(level+1) + f'Azimuth = {self.azimuth},  Tilt = {self.tilt}, Roll = {self.roll}\n');
        #self.camlens.print (level+1);
        
        return
