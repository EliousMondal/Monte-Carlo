'''Author - MD. ELIOUS ALI MONDAL
   Created - 03/06/2020
   Description - Function to adjust the dr_max after each MC cycle.'''

##==============================================================================
def dr_max_adjust(move_ratio,dr_max):
    '''Input - move_ratio and dr_max at present cycle
       Output - modified dr_max to keep  0.45<move_ratio<0.55'''
    if (move_ratio > 0.55):
        return dr_max*1.05
    elif (move_ratio < 0.45):
        return dr_max*0.95
    else:
        return dr_max

##==============================================================================
