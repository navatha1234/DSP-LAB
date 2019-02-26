from matplotlib import pyplot as plt
import sounddevice as sd
import numpy as np
import scipy.io
from scipy.io import wavfile
[fs,data]=wavfile.read('go.wav')
x=data.astype(np.float32)
n=np.random.rand(len(x))
y=x+n*50
s=np.zeros(len(y))
for i in range(0,len(y)):
	s[i]=(np.sum(y[i:i+10]))/10.0
wavfile.write('original.wav',fs,x)
wavfile.write('noiced.wav',fs,y)
wavfile.write('avg.wav',fs,s)
x=x[10000:20000]
n=n[10000:20000]
y=y[10000:20000]
s=s[10000:20000]
plt.subplot (2,2,1)
plt.plot(x)
plt.subplot (2,2,2)
plt.plot(n)
plt.subplot (2,2,3)
plt.plot(y)
plt.subplot (2,2,4)
plt.plot(s)
plt.show()
