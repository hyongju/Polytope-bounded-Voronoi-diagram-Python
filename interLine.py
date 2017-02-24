#!/usr/bin/python

import numpy as np
from numpy.linalg import inv

#line1 = [0.1, 0.2, 0.1]
#line2 = [0.4, -0.2, 0.3]

def interLine(line1,line2):
    if (line1[0]*line2[1] - line2[0]*line1[1] != 0):
        A = np.matrix([[line1[0],line1[1]],[line2[0],line2[1]]])
        b = np.matrix([[line1[2]],[line2[2]]])
        return np.dot(inv(A),b)
    else:
        return False
