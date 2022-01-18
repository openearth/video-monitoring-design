# -*- coding: utf-8 -*-
"""
OrthographicImage
 
Class for a orthographic image (photo or drawing).
 
Constructor:
    OrthographicImage (filename, topleft, bottomright)
        filename    :: name of image file (TIFF, JPEG, etc)
        topleft     :: world XY coordinates (meters) of image corner
        bottomright	:: world XY coordinates (meters) of image corner
 
Methods:
    mapWorldToImage

"""

import matplotlib.pyplot as plt
import numpy as np

class OrthographicImage():
    
    def __init__ (self, filename, topleft, bottomright, epsg=' '):
        self.filename = filename;
        self.topleft = topleft;
        self.bottomright = bottomright;
        self.image = plt.imread (self.filename);
        self.epsg = epsg;

        pixels = np.empty((1,2)) * np.nan
        pixels[0,0] = np.size (self.image, 1)
        pixels[0,1] = np.size (self.image, 0)
        self.resolution = (np.array(bottomright) - np.array(topleft)) / pixels
        return
        
    def mapWorldToImage (self, xy):
        uv = (np.array(xy) - np.array(self.topleft)) / self.resolution;
        return uv

