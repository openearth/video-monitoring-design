# -*- coding: utf-8 -*-
"""
Make a plot  of the camera footprints on camera coordinates, 
and specific data is written to the console.
Convert world coordinates to local video coordinates and print
and plot.

"""

import numpy as np
import matplotlib.pyplot as plt
from mapWorldToSite import mapWorldToSite
from indent import indent

def plotCameraFootprintCamcoords (filename, ortho, loc, video, **kwargs): # center, shorelineAngle)
    
    #----------------------------------------------------------------------
    #   Plot camera locations on site, with camera coordinates
    fig, ax = plt.subplots(figsize=(12,6))
    center = kwargs['center']
    shorelineAngle = kwargs['shorelineAngle']
    lim = kwargs['ylimit']
    plt.xlim([-lim, lim])
    plt.ylim([-lim*0.1, lim])
    plt.grid(True)
    plt.xlabel('- y [m]')
    plt.ylabel('x [m]')
    ax.plot (0, 0, '+k');
    
    print ('\nWorld to Site corner coordinate mapping:\n')
    cameras = video.keys();
    for i in range(len(cameras)):
        print (indent(0) + f'{video[list(cameras)[i]][list(cameras)[i]].name[0]}'); 
        
        argco = np.empty ((6,2)) * np.nan;
        foot = video[list(cameras)[i]][list(cameras)[i]].footprint.XYfoot;  
        k = 0
        for j in [ 0, 1, 3, 4, 5 ]:
            argco[k,:] = mapWorldToSite (foot[j,:], center, shorelineAngle)
            print (indent(1) + f'{foot[j,0]:8.1f} {foot[j,1]:8.1f} -> {argco[k,0]:8.1f} {argco[k,1]:8.1f}');
            k += 1
        argco[4,:] = argco[0,:]
        
        plt.plot (argco[0,1], argco[0,0], 'ok', markersize=10);
        for k in range(4):
            ax.plot (argco[k,1], argco[k,0], '*b')
            if video[list(cameras)[i]][list(cameras)[i]].footprint.overHorizon:
                color = 'g'
            else:
                color = 'b'
            ax.plot ([argco[k,1], argco[k+1,1]], [argco[k,0], argco[k+1,0]], c=color);
        print('\n')
    
    plt.savefig(filename)
    return

