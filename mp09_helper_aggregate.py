"""
Helper script for mp09 bash script
aggregates R2 and MTsat data at each of 14 surfaces
saves one csv file per subject

Clara Weber MD
sometime 2026
"""

import numpy as np
import pandas as pd
import nibabel as nib
import sys

subj = sys.argv[1]

pth = 'outputs/equivols'

depths = [0.0, 0.07692307692307693, 0.15384615384615385, 0.23076923076923078, 0.3076923076923077, 0.38461538461538464, 0.46153846153846156, 0.5384615384615384, 0.6153846153846154, 0.6923076923076923, 0.7692307692307693, 0.8461538461538461,  0.9230769230769231, 1.0]

data_subj = []
for d in depths:
	data_lh = np.array(nib.load(f'{pth}/sub-{subj}_{d}_fsa5.lh.mgh').get_fdata()).flatten()
	data_rh = np.array(nib.load(f'{pth}/sub-{subj}_{d}_fsa5.rh.mgh').get_fdata()).flatten()
	data_subj.append(np.concatenate((data_lh, data_rh)))

pd.DataFrame(np.asarray(data_subj).T, columns = depths).to_csv(f'{pth}/{subj}_mtatdepths.csv')

data_subj_r2 = []
for d in depths:
	data_lh = np.array(nib.load(f'{pth}/sub-{subj}_{d}_r2_fsa5.lh.mgh').get_fdata()).flatten()
	data_rh = np.array(nib.load(f'{pth}/sub-{subj}_{d}_r2_fsa5.rh.mgh').get_fdata()).flatten()
	data_subj_r2.append(np.concatenate((data_lh, data_rh)))

pd.DataFrame(np.asarray(data_subj_r2).T, columns = depths).to_csv(f'{pth}/{subj}_r2atdepths.csv')