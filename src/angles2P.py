# -*- coding: utf-8 -*-
"""
angles2P, based on .m file

P = angles2P (x, y, z, azimuth, tilt, roll, width, height, hfov)

Compute Walton vector and P-matrix from camera position, orientation
and sensor/lens paramters for an prototypical camera. 

"""
import numpy as np

def angles2P (x, y, z, azimuth, tilt, roll, width, height, hfov):

    u0 = width/2;
    v0 = -height/2;

    f = (width/2) / (np.tan(np.deg2rad(hfov/2)));
    R = makeRot (azimuth, tilt, roll);
    L = - (x*R[2,0] + y*R[2,1] + z*R[2,2]);

    m = np.zeros(11)
    m[0]  = (u0*R[2,0] + f*R[0,0]) / L;
    m[1]  = (u0*R[2,1] + f*R[0,1]) / L;
    m[2]  = (u0*R[2,2] + f*R[0,2]) / L;
    m[3]  = -(m[0]*x + m[1]*y + m[2]*z);
    m[4]  = R[2,0] / L;
    m[5]  = R[2,1] / L;
    m[6]  = R[2,2] / L;
    m[7] = (v0*R[2,0] + f*R[1,0]) / -L;
    m[8]  = (v0*R[2,1] + f*R[1,1]) / -L;
    m[9] = (v0*R[2,2] + f*R[1,2]) / -L;
    m[10] = -(m[7]*x + m[8]*y + m[9]*z);

    P = np.array([[m[0], m[1], m[2],  m[3]],   
                  [m[7], m[8], m[9], m[10]],
                  [m[4], m[5], m[6],  1   ]])
    return P


def makeRot (a,t,r):
    
    A = [[ np.cos(np.deg2rad(a)), -np.sin(np.deg2rad(a)), 0 ], [  np.sin(np.deg2rad(a)), np.cos(np.deg2rad(a)),    0    ], [ 0,     0,       1    ]]
    B = [[    1      ,  0,    0 ], [     0,    np.cos(np.deg2rad(t)), np.sin(np.deg2rad(t)) ], [ 0, -np.sin(np.deg2rad(t)), np.cos(np.deg2rad(t)) ]]
    C = [[ np.cos(np.deg2rad(r)),  np.sin(np.deg2rad(r)), 0 ], [ -np.sin(np.deg2rad(r)), np.cos(np.deg2rad(r)),    0    ], [ 0,     0,      -1    ]]

    R = np.linalg.multi_dot([C, B, A])
    return R
