import numpy as np
import matplotlib.pyplot as plt
import cmath
dp=float(input("enter dp"))	
ds=float(input("enter ds"))


e=np.sqrt((1/(dp**2))-1)
a=np.arccosh((1/e)*np.sqrt((1/ds**2)-1))
b=np.arccosh(ws/wp)
w=np.arange(0,100,10)
h=1/(np.sqrt(1+(e**2)*(np.cos(n*np.arccos(w/wp)))**2))
if(w>wp):
	h=1/(np.sqrt(1+(e**2)*(np.cosh(n*np.arccosh(w/wp)))**2))
	plt.plot(w,h)
	plt.show()