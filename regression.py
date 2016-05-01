# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:50:06 2016

@author: Soham Shah
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
from sklearn import datasets, linear_model

X = np.array([1.0, 2.0, 2.5, 3.75, 5.2, 6.1, 7.0])
Y = np.array([2.25, 2.40, 3.94, 4.77, 6.02, 7.3, 8.1])

xp = np.linspace(0,10,1000)
p = np.polyfit(X,Y,1)
print p
p5 = np.polyfit(X,Y,3)
print p5
yfit = np.polyval(p,X)
yy = np.polyval(p5,X)

plt.plot(X,Y,'r.')
plt.plot(X,yfit, 'b-')
plt.plot(X,yy, 'm--')
plt.show()


yres = yfit - Y

SSresid = np.sum(np.power(yres,2))

print SSresid

SStot = len(Y)*np.var(Y)

rsq = 1 - SSresid/SStot
print "R square = ",rsq

yyres = yy -Y
SSr = np.sum(np.power(yyres,2))
rsq2 = 1 -SSr/SStot
print rsq2