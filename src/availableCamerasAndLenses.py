# -*- coding: utf-8 -*-
"""
availableCamerasAndLenses, based on .m file

[cam lens] = availableCamerasAndLenses ()

Return collections of available cameras and lenses used for video monitoring related application. 
A specific camera and lens will be mated using the CameraLens object (which checks compatibility).

"""
from Camera import Camera
from Lens import Lens

def availableCamerasAndLenses():
        
    cam = {}; #cam = [];
    lens = {}; #lens = [];

    cam['flea13']          = Camera ('PointGrey FL2G-13S2 ICX445 1/3inch',             3.75, 1288, 964);
    cam['flea14']          = Camera ('PointGrey FL2-14S3 ICX267 1/2inch',              4.65, 1392, 1032);
    cam['flea20']          = Camera ('PointGrey FL2-20S4 ICX274 1/1.8inch',            4.40, 1624, 1224);
    cam['flea50']          = Camera ('PointGrey FL2G-50S5 ICX655 2/3inch',             3.45, 2448, 2048);
    cam['flir50']          = Camera ('Blackfly S GigE BFS-PGE-50S5C-C IMX264 2/3inch', 3.45, 2448, 2048);
    cam['grass14']         = Camera ('PointGrey Grasshopper-14S5 ICX285 2/3inch',      6.45, 1384, 1036);
    cam['scor']            = Camera ('PointGrey Scorpion-SO14C ICX267 1/2inch',        4.65, 1392, 1032);
    cam['dragon']          = Camera ('PointGrey Dragonfly HICOL ICX204 1/3inch',       4.65, 1024, 768);
    cam['x700']            = Camera ('Sony DFW-X700 1/2inch',                          6.25, 1024, 768);
    cam['sscdc50p']        = Camera ('Sony SSC-DC50P 1/2inch',                         7.0 , 768,  576);
    cam['av5115']          = Camera ('Arecont AV5115DNAIv1 1/2.5inch',                 2.2 , 2592, 1944);

    lens['mm_8_mp']        = Lens ('Computar M0814-MP',        8, 2/3);
    lens['mm_9_mp']        = Lens ('Fujinon HF9HA-1B',         9, 2/3);
    lens['mm_12_mp']       = Lens ('Tamron M112FM12',         12, 1/1.2);
    lens['mm_12_5_mp']     = Lens ('Fujinon HF12.5HA-1B',   12.5, 2/3);
    lens['mm_16_mp']       = Lens ('Tamron 23FM16SP',         16, 2/3);
    lens['mm_25_mp']       = Lens ('Fujinon HF25HA-1B',       25, 2/3);
    lens['mm_35_mp']       = Lens ('Fujinon HF35SA-1',        35, 2/3);
    lens['mm_50_mp']       = Lens ('Fujinon HF50SA-1',        50, 2/3);
    lens['mm_75_mp']       = Lens ('Fujinon HF75SA-1',        75, 2/3);
    lens['mm_6']           = Lens ('Pentax C60607KP/H612A',    6, 1/2);
    lens['mm_6_mp']        = Lens ('Pentax C60636KP/H614-MQ',  6, 1/2);
    lens['mm_4_8_legacy']  = Lens ('Legacy 4.8 mm lens',    4.8, 1/2);
    lens['mm_6_legacy']    = Lens ('Legacy 6 mm lens',        6, 1/2);
    lens['mm_8_5_legacy']  = Lens ('Legacy 8.5 mm lens',    8.5, 1/2);
    lens['mm_9_legacy']    = Lens ('Legacy 9 mm lens',        9, 1/2);
    lens['mm_12_5_legacy'] = Lens ('Legacy 12.5 mm lens',  12.5, 1/2);
    lens['mm_25_legacy']   = Lens ('Legacy 25 mm lens',      25, 1/2);

    return [cam, lens]
