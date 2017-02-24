import numpy as np
from numpy import linalg as LA

def perpBisector2d(v1, v2):
    vm = np.array([0.0,0.0])
    v3 = np.array([0.0,0.0])
    vn = np.array([0.0,0.0])
    vm[0] = (v1[0] + v2[0])/2
    vm[1] = (v1[1] + v2[1])/2
    v3[0],v3[1] = v2[0] - v1[0],v2[1]-v1[1]
    vn[0],vn[1] = v3[0]/ LA.norm(v3,2),v3[1]/LA.norm(v3,2)
    Ad = vn
    bd = np.dot(vn,vm)

    if np.dot(Ad,v1) <= bd:
        A = Ad
        b = bd
    else:
        A = -Ad
        b = -bd
    return Ad,bd

