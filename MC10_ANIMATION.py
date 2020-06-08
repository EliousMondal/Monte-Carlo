'''Name - MD ELIOUS ALI MONDAL
   Created - 06/06/2020
   Description - Uses the RX,RY,RZ data generated to create an animation of the
                 MC simulation for the first 10000 cycles'''

import numpy as np
from numpy.random import normal as normal

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
import matplotlib

print('Loading RX')
xs = np.loadtxt('RX_data.txt',delimiter=',')
xs = np.array([xs[i] for i in range(10000)])
print(len(xs))
print('Loading RY')
ys = np.loadtxt('RY_data.txt',delimiter=',')
ys = np.array([ys[i] for i in range(10000)])
print(len(ys))
print('Loading RZ')
zs = np.loadtxt('RZ_data.txt',delimiter=',')
zs = np.array([zs[i] for i in range(10000)])
print(len(zs))
print('RX, RY, RZ loaded')

nfr = len(xs) # Number of frames
print('number of frames = ',nfr)
fps = 200 # Frame per sec

BOXL = (108/0.6)**(1/3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sct, = ax.plot([], [], [], "o", markersize=5)

def update(ifrm, xa, ya, za):
    sct.set_data(xa[ifrm], ya[ifrm])
    sct.set_3d_properties(za[ifrm])
    
ax.set_xlim(0,BOXL)
ax.set_ylim(0,BOXL)
ax.set_zlim(0,BOXL)

ani = animation.FuncAnimation(fig, update, nfr, fargs=(xs,ys,zs), interval=2000/fps)

fn = 'MC_10000_cycle_animation'
ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
plt.rcParams['animation.html'] = 'html5'
ani

plt.show()
