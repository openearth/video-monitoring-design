# -*- coding: utf-8 -*-
"""
findBoundary
utils for bounding box and box based on plot limits

"""


def findBoundingBox(points):
    x_coordinates, y_coordinates = zip(*points)

    return [[min(x_coordinates), min(y_coordinates)], 
            [max(x_coordinates), max(y_coordinates)]]


def plotBox(bbox, plot):
    box = [[],[]]
    box[0].append(plot[0][0] if bbox[0][0] < plot[0][0] or bbox[0][0] > plot[1][0] else bbox[0][0])
    box[0].append(plot[0][1] if bbox[0][1] < plot[0][1] or bbox[0][1] > plot[1][1] else bbox[0][1])
    box[1].append(plot[1][0] if bbox[1][0] > plot[1][0] or bbox[1][0] < plot[0][0] else bbox[1][0])
    box[1].append(plot[1][1] if bbox[1][1] > plot[1][1] or bbox[1][1] < plot[0][1] else bbox[1][1])
    
    return box
