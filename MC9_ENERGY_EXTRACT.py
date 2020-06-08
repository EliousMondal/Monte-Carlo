'''Author - MD ELIOUS ALI MONDAL
   Created - 05/06/20
   Description - extracting the energies from the data, calculating the standard
                 deviation and variance, and storing the RX,RY,RZ in smaller
                 cycle steps.'''

import numpy as np
import matplotlib.pyplot as plt

##==============================================================================
PE = np.loadtxt('PEn_data.txt',delimiter=',')
x = np.array([i for i in range(len(PE))])
a = np.mean(PE)
b = np.mean(PE**2)
v = b-a**2
std = np.sqrt(v)

print(len(x))
print(np.mean(a))
plt.figure()
plt.title('Stdandard deviation = %0.6f' %std)
plt.xlabel('No. of trials ----->')
plt.ylabel(r'<$\frac{E_{potential}}{n}$> (reduced units)----->')
plt.plot(x,PE,label=r'<$\frac{E_{potential}}{n}$> = %0.6f' %a)
plt.legend()
plt.show()

##==============================================================================
'''Extracting the positions and storing the positions again at an interval of
   500 cycles so as to make the position data compact. This part of code will
   only be executes after closing the graph generated above.'''

print('Loading RX, RY, RZ')
xs = np.loadtxt('RX_data.txt',delimiter=',')
ys = np.loadtxt('RY_data.txt',delimiter=',')
zs = np.loadtxt('RZ_data.txt',delimiter=',')
print('RX, RY, RZ loaded')

i = 0
a = len(xs)
index = []
while(i<a):
    index.append(i)
    i = i + 500

RX = np.array([xs[i] for i in index])
RY = np.array([ys[i] for i in index])
RZ = np.array([zs[i] for i in index])

RX_data = np.vstack([i for i in RX])
np.savetxt('RX_small_data.txt',RX_data,delimiter=',')
RY_data = np.vstack([i for i in RY])
np.savetxt('RY_small_data.txt',RY_data,delimiter=',')
RZ_data = np.vstack([i for i in RZ])
np.savetxt('RZ_small_data.txt',RZ_data,delimiter=',')

##==============================================================================
