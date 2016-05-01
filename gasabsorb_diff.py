# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\smdes\.spyder2\.temp.py
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

class ccgasabsorb:
    Lw0=100.0 # flow rate of water at top (kmoles/hr)
    Gc_bottom=50.0 #flow rate of methane at bottom kmoles/hr
    Gm_bottom=50.0  #flow rate of CO2 at bottom (kmoles/hr)
    Klc_list=0.5 # liquid side mass transfer coeff of CO2 cm/s Jingyi Han et al./Energy Procedia 37 ( 2013 )1728 – 1735
    Klc=(Klc_list)*0.01*3600 #mass transfer coeffof CO2
    Klm=62.2*0.001 #mass transfer coeffof methane hr^-1 Korean J. Chem. Eng., 32(6), 1060-1063 (2015), DOI: 10.1007/s11814-014-0341-7 Gas-liquid mass transfer coefficient of methane.

    Klw= 1.367*(10**-3)*3600 #mass transfer coeff of water m/hr #(Ref. Fundamentals of Heat Transfer by Incropera and DeWitt, Wiley, 5th Edition, 2002)  
    
    
    Hc_list=0.034 #listed henry's const for co2 mol/lit.atm
    Hm_list=0.014 # listed henry'sconst for methane mol/lit.atm source for all henry's constants http://www.mpch-mainz.mpg.de/~sander/res/henry.html Rolf Sander Air Chemistry Department, Max-Planck Institute of Chemistry
    Gc = Gc_bottom
    Gm = Gm_bottom

    Hc=((Hc_list)/101325.0) # convert to si
    Hm=Hm_list/101325.0
    Cc0=0
    Cm0=0
    Psat=3166.0# psat of water at 298K (Pa) from smith, van-ness & abbot, int to chem engg thermo, 7th ed. , appendix F:steam tables
    P=101325.0 # op. pressure Pa
    h=10.0
    A=1.0
    n=51
    dx=h/(n-1)
    print(dx)
    error=1.0
    Gc00=49.9 #guess value of Co2 flow rate at top 
    Gm00=49.9 # guess value of methane flow rate at top
    Gw00=0.2  # guess value of water vapour flow rate at top
    Gc0=Gc00
    Gm0=Gm00
    Gw0=Gw00
    Lw=Lw0
    x=h
    Cc=Cc0
    Cm=Cm0
    Lc = 0
    Lm = 0
    
    def f(q,pc,x):
        Lw,Lc,Lm,Gc,Gm,Gw, Cc,Cm = q
        Klw,Klm,Klc,Hc,Hm,P,Psat,A,h = pc
        yc=Gc/(Gc+Gm+Gw)
        ym=Gm/(Gc+Gm+Gw)
        yw=Gw/(Gc+Gm+Gw)
        diff = [-Klc*A*((P*yc*Hc)-(Cc)),-Klm*A*((P*ym*Hm)-(Cm)),Klw*A*((Psat-P*yw)/(8.314*298.16*1000)),-Klw*A*((Psat-P*yw)/(8.314*298.16*1000))]
        return diff
        n= 51
        dx = h/(n-1)
        x = np.arrange(0.0,h,dx)
        pc = [Klw,Klm,Klc,Hc,Hm,P,Psat,A,h]
        q=   [Lw,Lc,Lm,Gc,Gm,Gw, Cc,Cm]
        sol = odeint(diff,q,x,args=(pc))
        print "solution = ", sol[n]
        print sol[n,1]
        print sol[n,2]
        print sol[n,3]
        print sol[n,4]
        