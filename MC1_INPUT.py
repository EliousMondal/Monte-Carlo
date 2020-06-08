'''Author - MD. ELIOUS ALI MONDAL
   Created - 01/06/2020
   Description - Input file for Monte-Carlo simulation of 108 Ar atoms in NVT
   ensemble'''

import numpy as np
import numpy.random as random
random.seed(5)
import time

n = 108
ncycle = 1000
temp = 1.0
dens = 0.6
dr_max = 0.15
overlap = False
r_min = 0.75
sr2_ovr = 1/(r_min**2)
dens = 0.6
BOXL = (n/dens)**(1/3)
r_cut = 2.5/BOXL
r_cut_sq = r_cut**2
e_guard = 75
move_ratio = 0
n_moves = 0
n_trials = 0
n_pot_step = 0
acpot = 0
acpot_sq = 0
mr_dict = {}
drm_dict = {}
potn_dict = {}
acpot_dict = {}
acpotsq_dict = {}
