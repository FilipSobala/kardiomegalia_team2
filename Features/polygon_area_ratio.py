#!/bin/python3.11
import numpy as np
import skimage as ski
import sys 


def getConvexHull(img : np.ndarray):
    return ski.morphology.convex_hull_image(img)

def getConvexHullAreaRatio(img : np.ndarray):
    """assumptions: heart - 2's, lungs - 1's, background - 0's"""
    heartImg = img > 1
    lungsImg = img
    for x in np.nditer(lungsImg, op_flags=['readwrite']):
        if x == 2:
            x[...] = 0
    lungsImg = lungsImg > 0

    heartConvex = getConvexHull(heartImg)
    lungsConvex = getConvexHull(lungsImg)
    heartArea = np.sum(heartConvex)
    lungsArea = np.sum(lungsConvex)

    return heartArea / lungsArea
