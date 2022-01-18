# -*- coding: utf-8 -*-
"""
This script is an alternative Video monitoring Design Tool, work in progress.
The GUI has been traded in for an object-oriented script approach.
Objects for cameras and lenses, and site-specific things are
defined elsewhere, then this function is called to make a plot  of
the camera footprints over an orthographic image (e.g., aerial
photo) and specific data is written to the console.

"""

import matplotlib.pyplot as plt
import numpy as np

def plotCameraTable (filename, ortho, loc, video):
    
    #----------------------------------------------------------------------
    #   Plot camera locations and other data on table
    fig, ax = plt.subplots(figsize=(10,6), tight_layout={'pad':1})
    ax.axis('off')
    ax.axis('tight')
    plt.box(on=None)
    
    columns = (f' X$_{{{ortho.epsg}}}$ [m] ', f' Y$_{{{ortho.epsg}}}$ [m] ', ' z [m] ', ' azim [°] ', ' Hfov [°] ', ' tilt [°] ', ' roll [°] ', ' F. length [mm]')
    rows = list([])
    cell_text = list([])
    
    cameras = video.keys();
    for i in range(len(cameras)):
        x = video[list(cameras)[i]][list(cameras)[i]].location.x
        y = video[list(cameras)[i]][list(cameras)[i]].location.y
        z = video[list(cameras)[i]][list(cameras)[i]].location.z
        #uv = ortho.mapWorldToImage ([x, y])
        #u = uv[0,0]; v = uv[0,1]; 
        rows.append(list(cameras)[i])
        azim = video[list(cameras)[i]][list(cameras)[i]].azimuth
        tilt = video[list(cameras)[i]][list(cameras)[i]].tilt
        roll = video[list(cameras)[i]][list(cameras)[i]].roll
        hfov = video[list(cameras)[i]][list(cameras)[i]].camlens.hfov()
        Flength = video[list(cameras)[i]][list(cameras)[i]].camlens.lens.focalLength
        cell_text.append(['%1.1f' % x, '%1.1f' % y, '%1.1f' % z, str(azim), '%1.1f' % hfov, str(tilt), str(roll), str(Flength)])
    
    rcolors = plt.cm.BuPu(np.full(len(rows), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(columns), 0.1))
    
    the_table = plt.table(cellText=cell_text,
            rowLabels=rows,
            colLabels=columns,
            rowColours=rcolors,
            colColours=ccolors,
            loc='center')
    the_table.scale(1  , 1.5)
    the_table.auto_set_column_width([0,1,2,3,4,5,6,7,8,9])
    #the_table.set_fontsize(8)
    
    plt.savefig(filename, bbox_inches='tight', dpi=150) #, pad_inches = 0)
    return

