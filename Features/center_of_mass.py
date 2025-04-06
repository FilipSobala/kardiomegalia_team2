#!/bin/python3.11
import numpy as np
import skimage as ski
import sys 
import matplotlib.pyplot as plt



def getCenterOfMass(img : np.ndarray, tol=10): # seems to be working well with tol=10
    """assumptions: heart - 2's, lungs - 1's, background - 0's"""
    heartImg = img > 1
    contours = ski.measure.find_contours(heartImg, level=0.5)
    contour = max(contours, key=len)
    polygon = ski.measure.approximate_polygon(contour, tolerance=tol) 

    return calculateCenter(polygon)
    

def calculateCenter(polygon : np.ndarray) -> tuple:
    centerX = 0
    centerY = 0
    if polygon.shape[1] != 2:
        raise Exception("not 2-dimensional array")
    
    # first cord is Y - who tf came up with this shit #
    for cord in polygon:
        centerY += cord[0]
        centerX += cord[1]

    centerX /= polygon.shape[0]
    centerY /= polygon.shape[0]

    # ! (y,x)
    return (centerY, centerX) # return (centerX, centerY) #