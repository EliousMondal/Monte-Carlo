'''Author - MD. ELIOUS ALI MONDAL
   Created - 03/06/2020
   Description - A metropolis function is defined to judge the acceptance of
                 a random displacement of atom'''

from MC4_POTENTIAL_INDIVIDUAL import *

##==============================================================================
def metropolis(delta):
    '''Returns whether a move is accepted or rejected
       Input - delta: difference in E_potential between new and old configuration
       Ouput - True: if move accepted, False: if move rejected'''
    if (delta>e_guard):
        return False
    if (delta < 0):
        return True
    else:
        a = random.uniform(0,1)
        return np.exp(-delta) > a

##==============================================================================
