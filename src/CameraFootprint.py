# -*- coding: utf-8 -*-
"""
CameraFootprint, based on .m file

Class for the footprint of a mounted camera
The footprint is the area in view on the Z=0 plane

Constructor:
    CameraFootprint (mountedCamera)
    mountedCamera	:: reference to fixed and orientated camera
Methods:
    plot    : plot footprint on current figure using orthomap
    print   : pretty-print the camera/lens parameters

"""

import numpy as np
import matplotlib.pyplot as plt
from indent import indent
from normalize import normalize
from angles2P import angles2P
from extendLine import extendLine
from mapWorldToSite import mapWorldToSite
from mapUVtoXYatZ0 import mapUVtoXYatZ0

class CameraFootprint ():
    '''
    mountedCamera           # reference to camera
    XYfoot                  # calculated footprint
    overHorizon = false;    # true means top corners of footprint artificial
    
    lineExtention = 100;    # factor by which to extend surface projections of lines that go above the horizon
    '''
    
    def __init__ (self, mountedCamera):
        
        self.mountedCamera = mountedCamera
        self.lineExtention = 100
        self.overHorizon = False
        
        # Calculate the camera P-matrix and use it to project the seven
        # image points we are interested in.  The first is the top left
        # corner, then top right, mid right, lower right, lower left,
        # mid left and finally the image center.

        x = mountedCamera.location.x;
        y = mountedCamera.location.y;
        width  = mountedCamera.camlens.camera.imWidth;
        height = mountedCamera.camlens.camera.imHeight;

        P = angles2P ( x, y, 
                mountedCamera.location.z, 
                mountedCamera.azimuth, 
                90 - mountedCamera.tilt, 
                - mountedCamera.roll, 
                width, height, 
                mountedCamera.camlens.hfov() )

        UV = np.array([
               [0, 0],
               [width,   0],
               [width,   height/2],
               [width,   height],
               [0,       height],
               [0,       height/2],
               [width/2, height/2]
             ])

        XY = mapUVtoXYatZ0 (UV, P)

        # Determine whether the top edge of the image is above the
        # horizon and if so replace the top left and right points
        # with extentions of the sides based on the mid and lower
        # points.  (The mid points must be below the horizon for this
        # to work properly.)
        # The top edge is above the horizon if the projections of the
        # top corner and the image center are on opposite sides of
        # the line through the camera position perpendicular to the
        # azimuth.

        p1 = np.array([x, y, 1])
        xx = x + 10 * np.sin (np.deg2rad(mountedCamera.azimuth+90))
        yy = y + 10 * np.cos (np.deg2rad(mountedCamera.azimuth+90))
        p2 = np.array([xx, yy, 1])
        line = normalize (np.cross (p1, p2))

        dist1 = np.dot (line, np.array([XY[0,0], XY[0,1], 1]))
        dist2 = np.dot (line, np.array([XY[6,0], XY[6,1], 1]))

        if (np.sign(dist1) != np.sign(dist2)) and mountedCamera.tilt != 90:
            XY[0,:] = extendLine ([[XY[4,0]], [XY[4,1]], [1]], [[XY[5,0]], [XY[5,1]], [1]], self.lineExtention);
            XY[1,:] = extendLine ([[XY[3,0]], [XY[3,1]], [1]], [[XY[2,0]], [XY[2,1]], [1]], self.lineExtention);
            self.overHorizon = True;

        self.XYfoot = XY;
        return
       
        
    def plot (self, cname, ortho, color=[0, 0, 0]):

        for i in range(6):
            j = np.mod(i+1,6)
            
            uvi = ortho.mapWorldToImage (self.XYfoot[i,:])
            uvj = ortho.mapWorldToImage (self.XYfoot[j,:])

            plt.plot ([uvi[:,0], uvj[:,0]], [uvi[:,1], uvj[:,1]], c=color, linewidth=1.2)
        
            uv7 = ortho.mapWorldToImage (self.XYfoot[6,:])
            plt.plot (uv7[0,0], uv7[0,1], '+', c=color, linewidth=2)
            
            plt.text (uv7[0,0]+20, uv7[0,1]+20, cname, c=color, fontsize=12)

        plt.xlim(0, ortho.mapWorldToImage(ortho.bottomright)[0,0])
        plt.ylim(0, ortho.mapWorldToImage(ortho.bottomright)[0,1])
        plt.gca().invert_yaxis()
        return
    
    
    def printing (self, level=0):
        
        print(indent(level) + 'CameraFootprint:\n')
        self.mountedCamera.printing (level+1)
        
        print(' ' * (level+1) + 'Image projection coordinates:')
        if self.overHorizon:
            print (' ' * (level+2) + 'Top left and right are above the horizon')
        else:
            print (' ' * (level+2) + f'Top left     = [{self.XYfoot[0,0]:.1f}, {self.XYfoot[0,1]:.1f}]', )
            print (' ' * (level+2) + f'Top right    = [{self.XYfoot[1,0]:.1f}, {self.XYfoot[1,1]:.1f}]')
        print (' ' * (level+2) + f'Bottom right = [{self.XYfoot[3,0]:.1f}, {self.XYfoot[3,1]:.1f}]')
        print (' ' * (level+2) + f'Bottom left  = [{self.XYfoot[4,0]:.1f}, {self.XYfoot[4,1]:.1f}]')
        print (' ' * (level+2) + f'Image center = [{self.XYfoot[6,0]:.1f}, {self.XYfoot[6,1]:.1f}]\n')
        
        return
