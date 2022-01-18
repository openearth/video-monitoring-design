
import numpy as np

def mapWorldToSite (world, origin, a):
    
    s = np.sin(np.deg2rad(a+180));
    c = np.cos(np.deg2rad(a+180));
    x = - origin[0];
    y = - origin[1];

    T = np.array([ 
         [c, -s,  c*x-s*y],
         [-s, -c, -s*x-c*y],
         [0,  0,  1]
        ]);

    video = np.dot(T, np.append ( world, 1 ))
    video = video[0:2]
    
    return video 