# -*- coding: utf-8 -*-
"""
Make a plot  of the camera footprints on camera coordinates, 
and specific data is written to the console.
Convert world coordinates to local site coordinates and print
and plot.

"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from mapWorldToSite import mapWorldToSite
from findBoundary import findBoundingBox, plotBox
from indent import indent

def plotPixelResolution (foldername, ortho, loc, video, **kwargs): # center, shorelineAngle)
    
    #----------------------------------------------------------------------
    #   Plot pixel resolution on site, with camera coordinates
    plotsettings = kwargs
    center = plotsettings['center']
    shorelineAngle = plotsettings['shorelineAngle']
    ylim = plotsettings['ylimit']
    xlim = plotsettings['xlimit']
    z    = plotsettings['z']
    xlimNeg = -xlim*0.1
    
    nx = 100; ny = 100
    resmin = 0; resmax = 50
    
    print ('\nComputing Pixel resolution per camera')
    cameras = video.keys()
    newrange = np.argsort(np.abs(range(len(cameras))-np.sum(range(len(cameras)))/len(range(len(cameras)))))
    
    os.makedirs(foldername, exist_ok=True)
    
    argcos = {}
    pixres_cs = []; pixres_ls = []
    Xs = []; Ys = []
    for i in range(len(cameras)):
        
        # build footprint on world images
        argco = np.empty ((6,2)) * np.nan;
        foot = video[list(cameras)[i]][list(cameras)[i]].footprint.XYfoot;
        k = 0
        for j in [ 0, 1, 3, 4, 5 ]:
            argco[k,:] = mapWorldToSite (foot[j,:], center, shorelineAngle)
            k += 1
        argco[4,:] = argco[0,:]
        
        # get grid for surf, using bbox based on polygon and plot
        bbox = findBoundingBox(argco)
        box = plotBox(bbox, [[xlimNeg, -ylim],[xlim, ylim]]) 
        Xlin = np.linspace(box[0][0], box[1][0], ny)
        Ylin = np.linspace(box[0][1], box[1][1], nx)
        Y, X = np.meshgrid(Ylin, Xlin)
        
        # build mask
        Yflat = Y.flatten() 
        Xflat = X.flatten()
        points = np.vstack((Yflat, Xflat)).T
        path = Path(np.c_[argco[:-1,1], argco[:-1,0]])
        grid = path.contains_points(points)
        grid = grid.reshape((ny, nx))
        
        # find and plot pixel resolution
        R = np.sqrt(Y**2 + X**2 + z**2)
        thetaCam = np.arctan2(Y, X)
        hfovcam = video[list(cameras)[i]][list(cameras)[i]].camlens.hfov()
        NpixH = video[list(cameras)[i]][list(cameras)[i]].camlens.width()
        DX = ( np.deg2rad(hfovcam) * R ) / NpixH
        DY = 1. / (z / R) * ( np.deg2rad(hfovcam) * R ) / NpixH
        pixres_c = np.maximum(np.abs(DX * np.sin(-thetaCam)), np.abs(DY * np.cos(-thetaCam)))
        pixres_l = np.maximum(np.abs(DX * np.sin(np.pi/2-thetaCam)), np.abs(DY * np.cos(np.pi/2-thetaCam)))
        # apply mask
        pixres_c = np.ma.masked_where(~grid, pixres_c)
        pixres_l = np.ma.masked_where(~grid, pixres_l)
        
        argcos[str(i)] = argco
        Xs.append(X); Ys.append(Y)
        pixres_cs.append(pixres_c); pixres_ls.append(pixres_l)
        
    plotPixelResolutionCrossshore(Ys, Xs, pixres_cs, argcos, resmin, resmax, ylim, xlimNeg, xlim, newrange, foldername)
    plotPixelResolutionLongshore(Ys, Xs, pixres_ls, argcos, resmin, resmax, ylim, xlimNeg, xlim, newrange, foldername)
        
    print ('\nDone.')
    return


def plotPixelResolutionCrossshore (Ys, Xs, pixres_s, argcos, resmin, resmax, ylim, xlimNeg, xlim, newrange, foldername): 
    #----------------------------------------------------------------------
    #   Plot crossshore pixel resolution on site, with camera coordinates
    
    fig, ax = plt.subplots(figsize=(20,5))
    plt.xlim([-ylim, ylim])
    plt.ylim([xlimNeg, xlim])
    plt.xlabel('- y [m]')
    plt.ylabel('x [m]')
    ax.plot (0, 0, '+k')
    
    for ii in newrange:
        argco = argcos[str(ii)]
        X = Xs[ii]; Y = Ys[ii]
        pixres = pixres_s[ii];
        
        axpdx = ax.pcolormesh(Y, X, pixres, cmap='inferno', vmin=resmin, vmax=resmax, shading='nearest')
        axcdx = ax.contour(Y, X, pixres, [0.1, 0.25, 0.5, 1, 2, 4, 8, 15, 30], colors='w')
        
        for k in range(4):  # plot footprint
            ax.plot (argco[k,1], argco[k,0], '*w')
            ax.plot ([argco[k,1], argco[k+1,1]], [argco[k,0], argco[k+1,0]], c='0.7', linewidth=1);
        clippath = Path(np.c_[argco[:-1,1], argco[:-1,0]])
        patch = PathPatch(clippath, facecolor='none')
        ax.add_patch(patch)
        axpdx.set_clip_path(patch)
        for c in axcdx.collections:
            c.set_clip_path(patch)
        # if ii % 2 == 0: # one every two, to avoid crowdness
        ax.clabel(axcdx, fmt="%2.1f", use_clabeltext=True)
        
    
    plt.grid(True, linewidth=0.2)
    plt.title('Cross-shore pixel resolution [m]')
    fig.colorbar(axpdx, ax=ax)
    fig.savefig(os.path.join(foldername, 'crossshore-res.png'))

    return


def plotPixelResolutionLongshore (Ys, Xs, pixres_s, argcos, resmin, resmax, ylim, xlimNeg, xlim, newrange, foldername): 
    #----------------------------------------------------------------------
    #   Plot longshore pixel resolution on site, with camera coordinates
    
    fig, ax = plt.subplots(figsize=(20,5))
    plt.xlim([-ylim, ylim])
    plt.ylim([xlimNeg, xlim])
    plt.xlabel('- y [m]')
    plt.ylabel('x [m]')
    ax.plot (0, 0, '+k')
    
    for ii in newrange:
        argco = argcos[str(ii)]
        X = Xs[ii]; Y = Ys[ii]
        pixres = pixres_s[ii];
        
        axpdx = ax.pcolormesh(Y, X, pixres, cmap='inferno', vmin=resmin, vmax=resmax, shading='nearest')
        axcdx = ax.contour(Y, X, pixres, [0.1, 0.25, 0.5, 1, 2, 4, 8, 15, 30], colors='w')
        for k in range(4):  # plot footprint
            ax.plot (argco[k,1], argco[k,0], '*w')
            ax.plot ([argco[k,1], argco[k+1,1]], [argco[k,0], argco[k+1,0]], c='0.7', linewidth=1);
        clippath = Path(np.c_[argco[:-1,1], argco[:-1,0]])
        patch = PathPatch(clippath, facecolor='none')
        ax.add_patch(patch)
        axpdx.set_clip_path(patch)
        for c in axcdx.collections:
            c.set_clip_path(patch)
        ax.clabel(axcdx, fmt="%2.1f", use_clabeltext=True)

    plt.grid(True, linewidth=0.2)
    plt.title('Longshore pixel resolution [m]')
    fig.colorbar(axpdx, ax=ax)
    plt.savefig(os.path.join(foldername, 'longshore-res.png'))
    
    return
