from matplotlib import pyplot as plt
from conv1d import conv1d
import numpy as np
L1=input("enter length of X[n]:")
L2=input("enter length of h[n]:")
x=np.zeros(L1)
y=np.zeros(L2)
print "enter x[n] values:"
for i in range(0,L1):
	x[i]=input("")
print "enter y[n] values:"
for i in range(0,L2):
	y[i]=input("")
k=np.zeros(L1)
l=np.zeros(L2)
for i in range(0,L1):
	k[L1-i-1]=x[i]
print k
for i in range(0,L2):
	l[L2-i-1]=y[i]
print l
cxy1=conv1d(x,l)
cxy2=conv1d(k,y)
cyx1=conv1d(y,k)
cyx2=conv1d(l,x)
print cxy1
print cxy2
print cyx1
print cyx2
