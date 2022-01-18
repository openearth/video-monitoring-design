# -*- coding: utf-8 -*-
"""
Location

Class for a location in 1D- 2D- or 3D-Cartesian space.

Constructor:
    Location (name, x, y, z)
        name	:: descriptive string
        x       :: X-coordinate
        y       :: Y-coordinate (optional; if unspecified 1D point)
        z       :: Z-coordinate (optional; if unspecified 2D point)
 
    Methods:
        homo    : return a homogeneous coordinates representation
        print   : pretty-print the location

"""

from indent import indent
import numpy as np
from inspect import signature

class Location():

    def __init__(self, name, *xyz):
                
        self.name = name;
        self.dim = len(xyz) #nargin - 1;
        
        if self.dim == 0:
            print ('Too few arguments for a Location (an X coord is the least you can specify)')
        elif self.dim  == 1:
            self.x = xyz
        elif self.dim  == 2:
            self.x = xyz[0]
            self.y = xyz[1]
        elif self.dim  == 3:
            self.x = xyz[0]
            self.y = xyz[1]
            self.z = xyz[2]
        return
    
    def homo (self):
        homo = self.x;
        if self.dim == 1:
            homo = np.array([[self.x], [1]]);
        elif self.dim == 2:
            homo = np.array([[self.x], [self.y], [1]]);
        elif self.dim == 3:
            homo = np.array([[self.x], [self.y], [self.z], [1]]);
        return homo 
    
    
    def print (self, level=0, depth=0):

        print (indent(level) + f'Location: {self.name}');
        if depth > 0:
            if self.dim == 1:
                print(f' ({self.x})\n');
            elif self.dim == 2:
                print (indent(level) + f' ({self.x},{self.y})\n')
            elif self.dim == 3:
                print (indent(level) + f' ({self.x},{self.y},{self.z})\n')
            
        return
