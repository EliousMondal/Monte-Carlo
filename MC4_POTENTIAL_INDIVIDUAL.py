'''Author - MD ELIOUS ALI MONDAL
   Created - 02/06/2020
   Description - Calculates the potntial energy of an atom with all other atoms
'''

from MC3_POTENTIAL import *

##==============================================================================
def i_potential(i,RN):
    '''Input - ith atom, coordinates shifted ith atom RN
       Output - Potential energy of interaction of this atom with other atoms'''
    pot = 0
    for j in range(n):
        if j != i:
            X = RN[0] - RX[j]; X = X - round(X)
            Y = RN[1] - RY[j]; Y = Y - round(Y)
            Z = RN[2] - RZ[j]; Z = Z - round(Z)
            R2 = (X**2 + Y**2 + Z**2)
            
            if (R2<r_cut_sq):
                R2 = R2*(BOXL**2)
                R2I = 1/R2
                
                if (R2I>sr2_ovr):           #checking overlap
                    return (pot,True)
                
                R6I = R2I**3
                pot = pot + 4*R6I*(R6I-1)
                
    return (pot,False)
##==============================================================================

    
