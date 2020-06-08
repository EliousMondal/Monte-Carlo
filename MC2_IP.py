'''Author - MD ELIOUS ALI MONDAL
   Created - 01/06/2020
   Description - This file generates 108 fcc lattice positions and scales them
                 such that each site is occupied by an Argon atom. This is the
                 same file for coordinate generation as used in MD.
'''

from MC1_INPUT import *
##==============================================================================
'''Initial positions for the classical MD simulaion of 108 Argon atoms'''
nu = int(input('Enter the no. of unit cells: '))

c1 = [0,0,0]
c2 = [0.5*1/nu,0.5*1/nu,0]
c3 = [0,0.5*1/nu,0.5*1/nu]
c4 = [0.5*1/nu,0,0.5*1/nu]
c = [c1,c2,c3,c4]                                              ##first unit cell

cp = []                                   ##collection of all the lattice points

##construction of lattice from the unit cell
for Iz in range(0,nu):
    for Iy in range(0,nu):
        for Ix in range(0,nu):
            for ref in c:
                rx = ref[0] + Ix/nu
                ry = ref[1] + Iy/nu
                rz = ref[2] + Iz/nu
                cp.append([rx,ry,rz])

RX = np.array([i[0] for i in cp])*BOXL
RY = np.array([j[1] for j in cp])*BOXL
RZ = np.array([k[2] for k in cp])*BOXL

R_dict = {0:np.array([RX,RY,RZ])}   #storing position at each time step
#==============================================================================
