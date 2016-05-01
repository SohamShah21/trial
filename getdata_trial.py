# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\smdes\.spyder2\.temp.py
"""
import scipy
import win32com.client
import matplotlib.pyplot as plt
import numpy as np
x1 = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb= x1.Workbooks('ExamProblemData2.1.xlsx')
sheet = wb.Sheets('ExamProblemData')

def getdata(sheet,Range):
    data = sheet.Range(Range).Value
    data = scipy.array(data)
    data = data.reshape((1,len(data)))[0]
    return data
    
t = getdata(sheet, "A2:A11")
ca = getdata(sheet, "B2:B11")
cb = getdata(sheet, "C2:C11")

p = np.polyfit(t,cb,3)
pa = np.polyfit(t,ca,3)
print p

plt.plot(t,cb,'ro')
cbfit = np.polyval(p,t)
plt.plot(t,cbfit,'b--')
plt.xlabel('t')
plt.ylabel('cb')
plt.show()
def rate(p,t):
    rate = p[0]*3*t*t + p[1]*t*2 + p[2]
    return rate
n = len(t)
k=[]

r=[]
for i in range (0,n):
    r[i] =rate(p,t[i])
    ca[i] = np.polyval(pa,t[i])
    cb[i] = np.polyval(p,t[i])
    k[i] = r[i]/(ca[i])
print k
k_avg = np.average(k)
    
    

