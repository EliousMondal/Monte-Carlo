'''Author - MD ELIOUS ALI MONDAL
   Created - 04/06/2020
   Description - Imports all the functions, does the Monte Carlo simulation
                 and stores all the data
'''
import sys
from MC5_METROPOLIS import *
from MC6_RANDOM_TRANSLATE import *
from MC7_ADJUST_DRMAX import *

start = time.time()
pot = EPOT[0]
print('Total number of cycles = ',ncycle)

##==============================================================================
for ncyc in range(ncycle):
    
    n_moves = 0
    for atom in range(n):
        old = i_potential(atom,(RX[atom],RY[atom],RZ[atom]))
        partial_pot_old = old[0]
        overlap = old[1]
        
        if overlap:
            print('overlap in the initial_old configuration at cycle = ',ncyc)
            sys.exit('OVERLAP')
        
        a = random_translate((RX[atom],RY[atom],RZ[atom]),dr_max)
        new = i_potential(atom,a)
        partial_pot_new = new[0]
        overlap = new[1]
        
        if (not overlap):
            delta_pot = partial_pot_new - partial_pot_old
            delta = delta_pot / temp
            
            if (metropolis(delta)):
                pot = pot + delta_pot
                RX[atom],RY[atom],RZ[atom] = a
                n_moves = n_moves + 1
                n_pot_step = n_pot_step + 1
                EPOT[n_pot_step] = pot
                
        n_trials = n_trials + 1
        potn = pot/n; potn_dict[n_trials] = potn
        acpot = acpot + potn; acpot_dict[n_trials] = acpot
        acpot_sq = acpot_sq + (potn**2); acpotsq_dict[n_trials] = acpot_sq
        
    R_dict[ncyc] = np.array([RX*BOXL,RY*BOXL,RZ*BOXL])
    move_ratio = n_moves/n
    mr_dict[ncyc] = move_ratio
    drm_dict[ncyc] = dr_max
    dr_max = dr_max_adjust(move_ratio,dr_max)
    print('Cycle ',ncyc,' done with move ratio ',move_ratio,' and potn ',potn)

pot_av = acpot/n_trials
print ('pot_av = ',acpot/n_trials)
acsq_av = acpot_sq/n_trials
print ('acpot_sq_av = ',acsq_av)
acpot_sq = acsq_av - (pot_av**2)
print ('deviation = ',acpot_sq)

print('Thr final configuration is ')
print(RX,RY,RZ)
end = time.time()
print('Time taken to execute the code is ',end-start,' seconds')

##==============================================================================
'''Storing the positions and potential data in files'''
ss = time.time()
RX_array = np.array([R_dict[its][0] for its in list(R_dict.keys())])
RX_data = np.vstack([i for i in RX_array])
np.savetxt('RX_data.txt',RX_data,delimiter=',')

RY_array = np.array([R_dict[its][1] for its in list(R_dict.keys())])
RY_data = np.vstack([i for i in RY_array])
np.savetxt('RY_data.txt',RY_data,delimiter=',')

RZ_array = np.array([R_dict[its][2] for its in list(R_dict.keys())])
RZ_data = np.vstack([i for i in RZ_array])
np.savetxt('RZ_data.txt',RZ_data,delimiter=',')

np.savetxt('PE_data.txt',list(EPOT.values()),delimiter=',')
np.savetxt('PEn_data.txt',list(potn_dict.values()),delimiter=',')
np.savetxt('PEn_ac_data.txt',list(acpot_dict.values()),delimiter=',')
np.savetxt('PEn_acsq_data.txt',list(acpotsq_dict.values()),delimiter=',')
np.savetxt('move_ratio_data.txt',list(drm_dict.values()),delimiter=',')
np.savetxt('drmax_data.txt',list(mr_dict.values()),delimiter=',')
se = time.time()
print('Time required to save the data is ',se-ss,' seconds.')
##==============================================================================
