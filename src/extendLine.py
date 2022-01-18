# -*- coding: utf-8 -*-
"""
p = extendLine (p1, p2, k)

Function to take the line defined by two homogeneous points and
compute a point K units further down the line. One unit is the
distance between the first and second points.  Returns the result
in homogeneous coordinates.

"""

import numpy as np
from normalize import normalize

def extendLine (p1, p2, k):
    
    p1 = normalize (p1);
    p2 = normalize (p2);
    pp = np.column_stack([
        (p1[0] + k*(p2[0]-p1[0])),
        (p1[1] + k*(p2[1]-p1[1])),
        1+k
        ]);

    p = pp[:,0:2]    
    
    return p
