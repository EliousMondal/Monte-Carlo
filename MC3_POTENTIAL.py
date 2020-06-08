'''Author - MD ELIOUS ALI MONDAL
   Created - 1/6/2020
   Description - This file calculates the potential energy of the initial
                 configuration.
'''
from MC2_IP import *

RX=RX/BOXL; RY = RY/BOXL; RZ=RZ/BOXL
##==============================================================================
def potential(x,y,z):
    '''Input: x,y,z = positions coordinates of the atoms
       Outout: epot = final potential energy of the configuration (x,y,z)'''
    pot = 0    #initialising the potential energy
    overlap = False
    
    for i in range(n-1):
        for j in range(i+1,n):
            
            X = (x[i] - x[j]); X = X - round(X)
            Y = (y[i] - y[j]); Y = Y - round(Y)
            Z = (z[i] - z[j]); Z = Z - round(Z) 
            R2 = (X**2 + Y**2 + Z**2)
            
            if (R2<r_cut_sq):
                R2 = R2*(BOXL**2)
                R2I = 1/R2
                
                if (R2I>sr2_ovr):           #checking overlap
                    overlap = True
                    return
                
                R6I = R2I**3
                pot = pot + 4*R6I*(R6I-1)
                
    return pot

EPOT = {0:potential(RX,RY,RZ)}  #dictionary to store EPOT at each accepted step
print('Potential energy for the initial configuration is ',EPOT[0],' reduced units')    
##==============================================================================

