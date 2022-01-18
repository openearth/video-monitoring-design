# -*- coding: utf-8 -*-
"""

This script is an alternative Video monitoring Design Tool, work in progress.
The GUI has been traded in for an object-oriented script approach.
Objects for cameras and lenses, and site-specific things are
defined elsewhere, then this function is called to make a plot  of
the camera footprints over an orthographic image (e.g., aerial
photo) and specific data is written to the console.

"""

import numpy as np
import matplotlib.pyplot as plt

def plotCameraFootprint (filename, ortho, loc, video):
    
    #----------------------------------------------------------------------
    #   Plot camera locations on the orthographic image of the site
    fig, ax = plt.subplots()
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.imshow (ortho.image)
    fig.set_size_inches(fig.get_size_inches()*3)
    
    locations = loc.keys();
    for i in range(len(locations)):
        uv = ortho.mapWorldToImage ([loc[list(locations)[i]].x, loc[list(locations)[i]].y]);
        ax.plot (uv[0,0], uv[0,1], 'or');
    
    #----------------------------------------------------------------------
    #   Calculate and plot the camera footprints

    colors = np.array([
        [1.0, 1.0, 0.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [0.0, 0.0, 0.0],
        ])

    cameras = video.keys();
    for i in range(len(cameras)):
        video[list(cameras)[i]][list(cameras)[i]].footprint.printing()
        video[list(cameras)[i]][list(cameras)[i]].footprint.plot (list(cameras)[i], ortho, colors [0+np.mod(i,np.size(colors,0)),:])
    
    plt.savefig(filename, bbox_inches='tight')#, pad_inches = 0)
    return

