
import numpy as np
import matplotlib.pyplot as plt
from CameraLens import CameraLens 
from availableCamerasAndLenses import availableCamerasAndLenses
from OrthographicImage import OrthographicImage
from Location import Location
from MountedCamera import MountedCamera
from plotCameraFootprint import plotCameraFootprint
from plotCameraTable import plotCameraTable
from plotCameraFootprintCamcoords import plotCameraFootprintCamcoords
from plotPixelResolution import plotPixelResolution
from availableCamerasAndLenses import availableCamerasAndLenses
from indent import indent
from mapWorldToSite import mapWorldToSite

def PROTOTYPE (scenario=1):
   
    sitename = 'PROTOTYPE';
    EPSG = 'utm'


    #----------------------------------------------------------------------
    #   Load available cameras and lensen and create combinations we want
    #   to use at this site
    
    [cam, lens] = availableCamerasAndLenses();
    
    camlens = dict();
    camlens['mp_2_mm_9']    = CameraLens (cam['flea20'], lens['mm_9_mp']);
    camlens['mp_5_mm_9']    = CameraLens (cam['flea50'], lens['mm_9_mp']);
    camlens['mp_2_mm_12_5'] = CameraLens (cam['flea20'], lens['mm_12_5_mp']);
    camlens['mp_5_mm_12_5'] = CameraLens (cam['flea50'], lens['mm_12_5_mp']);
    camlens['mp_5_mm_16']   = CameraLens (cam['flea50'], lens['mm_16_mp']);
    camlens['mp_5_mm_25']   = CameraLens (cam['flea50'], lens['mm_25_mp']);
    camlens['mp_5_mm_35']   = CameraLens (cam['flea50'], lens['mm_35_mp']);
    camlens['mp_5_mm_50']   = CameraLens (cam['flea50'], lens['mm_50_mp']);
    camlens['mp_5_mm_75']   = CameraLens (cam['flea50'], lens['mm_75_mp']);

    printCollection (['Cameras used at ' + sitename + ':'], camlens);

    
    #----------------------------------------------------------------------
    #   Load an orthographic image onto which to plot the results,
    #   create locations and cameras for the specific site and
    #   then plot the footprints.


    ortho = OrthographicImage ('PROTOTYPE-1.tiff', [581069, 5773543], [586803, 5766424]);

    loc = dict();
    loc['hotel'] =   Location ('Hotel', 583766, 5769540, 25);

    def videocam (name, location, azimuth, tilt, roll, camlens):
        video = dict()
        video[name] = MountedCamera ([sitename + ' ' + name], location, azimuth, tilt, roll, camlens)
        return video

    video = dict()
    if scenario == 1:
        video['C1'] = videocam ('C1', loc['hotel'],   32,  2.0, 0, camlens['mp_5_mm_50']);
        video['C2'] = videocam ('C2', loc['hotel'],   12,  2.0, 0, camlens['mp_5_mm_12_5']);
        video['C3'] = videocam ('C3', loc['hotel'],  335,  5.0, 0, camlens['mp_5_mm_9']);
        video['C4'] = videocam ('C4', loc['hotel'],  292,  5.0, 0, camlens['mp_5_mm_9']);
        video['C5'] = videocam ('C5', loc['hotel'],  253,  2.0, 0, camlens['mp_5_mm_12_5']);
        video['C6'] = videocam ('C6', loc['hotel'],  228,  2.0, 0, camlens['mp_5_mm_25']);
    else:
        print (f'Scenario {scenario} not defined')
    
    fn_footprint = 'footprint.png'
    plotCameraFootprint (fn_footprint, ortho, loc, video)
    
    fn_table = 'table.png'
    plotCameraTable (fn_table, ortho, loc, video)
    
    #----------------------------------------------------------------------
    #   Convert world coordinates to local video monitoring coordinates and print
    #   and plot.  The shoreline slope (site positive Y) is approximately
    #   30 degrees (compass heading).
    
    center = [loc['hotel'].x, loc['hotel'].y];
    zCam = 41.29
    shorelineAngle = 37. 
    lim = 4000 # ylimits around center
    
    plotCameraFootprintCamcoords ('worldcoords.png',ortho, loc, video, 
                                  center=center, 
                                  shorelineAngle=shorelineAngle,
                                  ylimit=lim)
    
    #----------------------------------------------------------------------
    #   Find pixel horz. and vert. resolution and plot on world coordinates 
    #   Table should also be printed later on.
    lim = 2500 # ylimits around center
    offshoreLim = 2000
    
    plotPixelResolution ('resolution',ortho, loc, video, 
                                  center=center, 
                                  shorelineAngle=shorelineAngle,
                                  ylimit=lim,
                                  xlimit=offshoreLim,
                                  z=zCam)
    
    return

def printCollection (title, struct):
    print (str(title)+ '\n');
    x = struct.keys();
    for i in range(len(x)):
        struct[list(x)[i]].print(0);
    return
