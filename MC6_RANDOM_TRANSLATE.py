'''Author - MD. ELIOUS ALI MONDAL
   Created - 03/06/2020
   Description - A function is defined to caarry out the random displacement
                 of an atom with periodic boundary conditions.
'''

from MC1_INPUT import *

##==============================================================================
def random_translate(a,dr_max):
    '''Gives an atom at a random displacement
       Input - Takes in position a = (x,y,z)
       Output - Returns new coordinate(xn,yn,zn) with random displacement'''
    r = random.uniform(-1,1,size=3)*dr_max/BOXL #uniform random numbers in (-1,1)
    xn = a[0] + r[0]; xn = xn%1
    yn = a[1] + r[1]; yn = yn%1
    zn = a[2] + r[2]; zn = zn%1
    return (xn,yn,zn)

##==============================================================================


