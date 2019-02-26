import matplotlib.pyplot as plt
import numpy as np
p=complex(0,1)
x=[1,1,1,1,1,1]
N=1000
X=[ ]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	b=0
	for n in range(0,len(x)):
		b=b+(x[n]*np.exp(-n*w[i]*p))
	X.append(b)
		
plt.figure(1)
plt.plot(w,np.abs(X))
plt.xlabel('freuency')
plt.ylabel('magnitude')
plt.grid()
plt.figure(2)
plt.plot(w,np.angle(X))
plt.grid()
plt.show()
