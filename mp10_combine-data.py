"""
get from one csv per subject to one csv for each depth, mean, std
this is based on statistical moments from casey paquola's cortpro toolbox
if it's inefficient but it works is it really inefficient

Clara Weber MD
sometime 2026
"""

import numpy as np
import pandas as pd
import nibabel as nib
import sys


pth = 'outputs/equivols'
# read subjlist
subjs = pd.read_csv(f'{pth}/scripts/surf_pipeline/subjlist.csv', dtype = 'str')['subjs'].values

# define depths
depths = ['0.0', '0.07692307692307693', '0.15384615384615385', '0.23076923076923078', '0.3076923076923077', '0.38461538461538464', '0.46153846153846156', '0.5384615384615384', '0.6153846153846154', '0.6923076923076923', '0.7692307692307693', '0.8461538461538461',  '0.9230769230769231', '1.0']

for mod in ['mt', 'r2']:
    # create empty lists
    data_moment1 = []
    data_moment2 = []
    data_pial = []
    data_d1 = []
    data_d2 = []
    data_d3 = []
    data_d4 = []
    data_d5 = []
    data_d6 = []
    data_d7 = []
    data_d8 = []
    data_d9 = []
    data_d10 = []
    data_d11= []
    data_d12 = []
    data_white = []

    for subj in subjs:
        # read csv
        subj_df = pd.read_csv(f'{pth}/{subj}_{mod}atdepths.csv')
        
        moment1 = np.mean(subj_df[depths[1:13]].values, axis = 1)
        data_moment1.append([subj, *moment1])

        moment2 = np.std(subj_df[depths[1:13]].values, axis = 1, ddof = 1)
        data_moment2.append([subj, *moment2])

        subj_pial = subj_df[depths[0]].values
        data_pial.append([subj, *subj_pial])

        subj_d1 = subj_df[depths[1]].values
        data_d1.append([subj, *subj_d1])

        subj_d2 = subj_df[depths[2]].values
        data_d2.append([subj, *subj_d2])

        subj_d3 = subj_df[depths[3]].values
        data_d3.append([subj, *subj_d3])

        subj_d4 = subj_df[depths[4]].values
        data_d4.append([subj, *subj_d4])

        subj_d5 = subj_df[depths[5]].values
        data_d5.append([subj, *subj_d5])

        subj_d6 = subj_df[depths[6]].values
        data_d6.append([subj, *subj_d6])

        subj_d7 = subj_df[depths[7]].values
        data_d7.append([subj, *subj_d7])

        subj_d8 = subj_df[depths[8]].values
        data_d8.append([subj, *subj_d8])

        subj_d9 = subj_df[depths[9]].values
        data_d9.append([subj, *subj_d9])

        subj_d10 = subj_df[depths[10]].values
        data_d10.append([subj, *subj_d10])

        subj_d11 = subj_df[depths[11]].values
        data_d11.append([subj, *subj_d11])

        subj_d12 = subj_df[depths[12]].values
        data_d12.append([subj, *subj_d12])

        subj_white = subj_df[depths[13]].values
        data_white.append([subj, *subj_white])
    
    # save csvs
    pd.DataFrame(data_moment1).to_csv(f'{pth}/{mod}_moment1.csv')
    pd.DataFrame(data_moment2).to_csv(f'{pth}/{mod}_moment2.csv')
    pd.DataFrame(data_pial).to_csv(f'{pth}/{mod}_pial.csv')
    pd.DataFrame(data_white).to_csv(f'{pth}/{mod}_white.csv')
    pd.DataFrame(data_d1).to_csv(f'{pth}/{mod}_depth1.csv')
    pd.DataFrame(data_d2).to_csv(f'{pth}/{mod}_depth2.csv')
    pd.DataFrame(data_d3).to_csv(f'{pth}/{mod}_depth3.csv')
    pd.DataFrame(data_d4).to_csv(f'{pth}/{mod}_depth4.csv')
    pd.DataFrame(data_d5).to_csv(f'{pth}/{mod}_depth5.csv')
    pd.DataFrame(data_d6).to_csv(f'{pth}/{mod}_depth6.csv')
    pd.DataFrame(data_d7).to_csv(f'{pth}/{mod}_depth7.csv')
    pd.DataFrame(data_d8).to_csv(f'{pth}/{mod}_depth8.csv')
    pd.DataFrame(data_d9).to_csv(f'{pth}/{mod}_depth9.csv')
    pd.DataFrame(data_d10).to_csv(f'{pth}/{mod}_depth10.csv')
    pd.DataFrame(data_d11).to_csv(f'{pth}/{mod}_depth11.csv')
    pd.DataFrame(data_d12).to_csv(f'{pth}/{mod}_depth12.csv')
