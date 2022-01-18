'''
   function normX = normalize (X)

   Function to normalize a point or line in homogeneous coordinates.

'''

import numpy as np

def normalize (X):
    normX = np.divide(X, X[-1]);
    return normX 