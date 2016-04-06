# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\smdes\.spyder2\.temp.py
"""

import math
Qk = input("Kerosene flow rate in m3/hr: ")
Qw = input("Water flow rate in m3/hr: ")
dk = 800 # kg/m3 density of kerosene
dw = 1000 # density of water
nk = 0.00164
nw = 0.001
ift = 0.052
Ce1 = input("concentration of EtSH at inlet ppm: ")
Cp1 = input("concentration of PrSH at inlet ppm: ")
Cb1 = input("concentration of BuSH at inlet ppm: ")
Cm_out = input("required concnetraiton of mercaptans at outlet ppm:")

dp = 1.15*((ift/((dw-dk)*9.81))**0.5)
c = input("weight fraction of base in water: ") # wt.fraction of base NaOH

'''
Distribution Coefficients
'''
Pet = 162
Ppr = 30
Pbu = 5

ap = input("size of packings (input one if column is unpacked) : ")
if ap == 1:
    ap = 1
    trt = 1 # totrtuosity
    vdfr = 1
else:
    trt = ap*dp*0.5
    vdfr = input("void factor of packings:")
v = Qk/Qw

#Vc = Qk/(math.pi*(D**2)*0.25*3600)
#Vd = Qw/(math.pi*(D**2)*0.25*3600)
#Re_disp = dw*Vd*dp/nw
#Cd = (24/Re_disp)
Vk = 0.33*((dw-dk)**0.4)*(dw**-0.6)*(dp**-0.8)*(nk**0.2)*(vdfr/ap)    
phi = 0.5
Vso = (dw-dk)*dp*dp*9.81/(18*nk)
Vdf = 0.1*Vso
Vcf = 0.2*Vso
cosine = (math.cos(0.25*trt*math.pi))**-2
error = 10
'''
Calculation of Flooding Velocity using Siebert fair model
'''

while (error > 0.00000001):
    Vcf =((0.192*Vso*vdfr)-(cosine)*Vdf)/1.08
    error = (phi - ((Vdf*cosine)/((vdfr*Vso*math.exp(-1.92*phi)) - (Vcf/(1-phi)))))**2
    Vdf = Vdf - (error*0.1)
    phi = phi - error*0.01
    
print "Vcf = ", Vcf
print "Vdf = ", Vdf
print "hold up = ", phi
print "error in hold up = ", error
'''
Calculation of diameter from known flooding velocity
'''
D =(((Qk+Qw)*4)/0.6*(Vcf+Vdf)*math.pi)**0.5 ## taking actual velocity as 0.6 of flooding velocity
Vc = Qk/(math.pi*(D**2)*0.25*3600)
Vd = Qw/(math.pi*(D**2)*0.25*3600)
Re_disp = dw*Vd*dp/nw
Cd = (24/Re_disp)
Vslip = Vk*(1-phi)
Ac = 0.25*(D**2)*math.pi
print "Diameter of Column = ", D
'''
Calculation of mass transfer coefficients
'''
Aet = 4.23
Apr = 7.756
Abu = 17.58
A1 = (0.95+c)**4.119
A2 = (ap/vdfr)**0.091
A3 = (100*Vd)**0.837
Kod_e = Aet*A1*A2*A3
Kod_b = Abu*A1*A2*A3
Kod_p = Apr*A1*A2*A3
# print Kod_e
ye = 0
yp = 0
yb = 0
Ce = Ce1
Cp = Cp1
Cb = Cb1
h=0
dh = 0.5
A = []
B=[]
C=[]
D=[]
while Ce+Cp+Cb > Cm_out:
    A.append(Ce)
    B.append(Cp)
    C.append(Cb)
    D.append(h)
    if Ce < 0:
        Ce = 0
    if Cp < 0:
        Cp = 0
    if Cb < 0:
        Cb = 0
    dne = Kod_e*(Pet*Ce)*Ac*dh*3600*(10**-6)
    dnp = Kod_p*(Ppr*Cp)*Ac*dh*3600*(10**-6)
    dnb = Kod_b*(Pbu*Cb)*Ac*dh*3600*(10**-6)
    Ce = Ce - dne/Qk
    Cp = Cp - dnp/Qk
    Cb = Cb - dnb/Qk
    ye = ye+(dne/Qw)
    yp = yp + (dnp/Qw)
    yb = yb + (dnb/Qw)
    c= c- (dne+dnp+dnb)/(1000000*Qw/40)
    h = h+dh
    
from pylab import plot,show
plot(D,A)
plot(D,B)
plot(D,C)
show()
print "Ce = ",Ce
print "Cp = ",Cp
print "Cb = ",Cb
print "h = ",h
print "c = ",c
