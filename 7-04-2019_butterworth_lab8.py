import numpy as np
import matplotlib.pyplot as plt
dp=float(input("enter dp"))
ds=float(input("enter ds"))
wp=float(input("enter wp"))
ws=float(input("enter ws"))
e=1/(ds**2-1)
f=1/(dp**2-1)
if (wp<ws):
	m=np.log10(e/f)
	s=m/2
	r=np.log10(ws/wp)
	n=np.ceil(s/r)
	print n
	wc=wp/(e**(1/(2*n)))
	print wc
	w=np.arange(0,1000,100)
	l=1+((w/wc)**(2*n))
	x=1/np.sqrt(l)
	plt.plot(w,x)
	plt.show()

	
		

