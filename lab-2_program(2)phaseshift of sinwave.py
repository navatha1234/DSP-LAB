import matplotlib.pyplot as plt
import numpy as a
fs=200
f=20
x=a.arange(0,50,0.5)
y=a.sin(2*a.pi*f*x/fs)
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('sinewave')
plt.xlabel('time')
plt.ylabel('amplitude')
z=a.sin(2*a.pi*f*x/fs+90)
plt.subplot(1,2,2)
plt.plot(x,z)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('phase shift sinwave')
plt.show()

