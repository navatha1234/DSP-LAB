import matplotlib.pyplot as plt
import numpy as np
x=[]
h=[]
y=[]
i=input("enter the interval range:")
j=input("enter the interval range:")
for n in range(0,i):
	a=int(input("enter the amplitude:"))
	x.append(a)
for p in range(0,j):
	b=input("enter the implse amplitude:")
	h.append(b)
for k in range(0,i+j-1):
	sum1=0
	for l in range(0,i):
		if(k-l>=0 and k-l<j):
			sum1=sum1+x[l]*h[k-l]
	y.append(sum1)
	print sum1
print y 
plt.plot(i,n)
plt.show()

