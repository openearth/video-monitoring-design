# -*- coding: utf-8 -*-
"""
XY = mapUVtoXYatZ0 (UV, P)

Function to convert an array of UV coordinates to and array XY
coordinates at Z=0 given a camera P-matrix.  Uses homogeneous
coordinates and a simplified P-matrix.  Because Z=0, one column of
the 3x4 matrix can be eliminated, resulting in an invertible 3x3
matrix.

"""

import numpy as np
from normalize import normalize 

def mapUVtoXYatZ0 (UV, P):
        
    XY = np.ones( np.shape (UV) ) * np.nan
    P124 = np.column_stack((P[:,0], P[:,1], P[:,3]))

    for i in range(np.size(UV,0)):
        uvh = np.append(UV[i,:], 1);  # convert to homo coords
        xy = normalize ( np.linalg.solve(P124, uvh));   # project to Z=0 plane (why Z=0?)
        XY[i,:] = xy[0:2];
        
    return XY
