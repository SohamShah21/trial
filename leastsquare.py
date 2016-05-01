# -*- coding: utf-8 -*-
"""
Created on Sun May 01 11:14:15 2016

@author: Soham Shah
"""
import scipy
import scipy.stats
import scipy.optimize
import math
import numpy as np
x = np.array([6.3, 9.3, 14.3, 21.3, 30.3, 41.2, 54.2])
Texp = np.array([70, 65, 58, 51, 45, 39, 36])

def f(X,p):
    f = p[0]*math.exp(x) + p[1]*math.exp(-x)
    return f
    
def error(X,Texp,Errdata):
    p = np.array[1,-2]
    T=f(X,p)
    resid = T - Texp
    return resid
    p0 = np.array[1,-2]
    popt = scipy.optimize.leastsq(f,p0, args=(x,Texp))
    print popt
    