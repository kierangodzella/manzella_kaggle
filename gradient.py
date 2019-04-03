import scipy
from scipy import signal
import math
import numpy as np

def gradient(image):
    #returns 3D array 
    m,n = np.shape(image)
    image = np.ndarray.astype(image, dtype = 'float')
    std = np.std(image)
    res_x = np.zeros([m,n])
    res_y = np.zeros([m,n])
    angle = np.zeros([m,n])
    magnitude = np.zeros([m,n])

    for i in range(1,m-1):
        for j in range(1,n-1):
            res_x[i,j] = (image[i,j-1] - image[i,j+1])
            res_y[i,j] = (image[i-1,j] - image[i+1,j])
            angle[i,j] = np.rad2deg(math.atan2(res_y[i,j],res_x[i,j]))
            magnitude[i,j] = np.sqrt(res_x[i,j]**2 + res_y[i,j]**2)
    
    return angle, magnitude



