"""
Prepare clinical data for MPM borderline project

June 2026
Clara Weber MD
"""
#%%
# housekeeping
import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer

pth = '/Users/cweber/Desktop/MPI/MPM/London'
#%%
# load data
df_raw = pd.read_csv(f'{pth}/AllData_Raw_csv.csv', sep = ',',  encoding='latin-1')

# list of all incl subjects (after preprocessing and QC)
subjects = list(pd.read_csv(f'{pth}/subjlist.csv')['Subject ID'].values)

# columns from df we actually need for aims 1,3
relevant_cols = list(pd.read_csv(f'{pth}/relevant_1.csv')['relevant_1'].values)

# recode subject IDs to consecutive numbers
df_recoding = pd.read_csv(f'{pth}/coding.csv')
recoding = dict(zip(df_recoding['Subject_ID'].values, df_recoding['consecutive'].values))
# %%
# filter only for included subjects
df_fsubj = df_raw[df_raw['ID'].isin(subjects)]

# filter only for relevant data
df_frel = df_fsubj[relevant_cols]

# replace subj IDs with consecutive ID
df_frel['ID'] = df_frel['ID'].replace(recoding).copy()
#%% 
# filter all cases with gender = 3 (these cases are described as transgender but no additional information, hence excluding)
df_fgen = df_frel[df_frel['Gender']!=3].copy()
#%%
# define renaming of misspelled medications
rename_dict_med = dict({
    '"Quiatapem" - Quetiapine?' : 'Quetiapine',
    'Qetiapine' : 'Quetiapine',
    'Quietapine' : 'Quetiapine',
    'Quintinipine': 'Quetiapine',
    'Quintinipine' : 'Quetiapine',
    'Respridone' : 'Risperidone',
    'acamprozate': 'Acamprosate',
    'Ariprapresole' : 'Aripiprazole',
    'Amatriptalin' : 'Amitriptyline',
    'Amatriptyline' : 'Amitriptyline',
    'Buproprian': 'Buproprion',
    'Citalapram' : 'Citalopram', 
    'Citalopam' : 'Citalopram',
    'Cutalapram' : 'Citalopram',
    'Citipram': 'Citalopram',
    'Citizine': 'other',
    'Diazapan' : 'Diazepam',
    'Estilapram': 'Escitalopram',
    'Floxatine' : 'Fluoxetine', 
    'Fluoxitine' : 'Fluoxetine', 
    'Fluxctine' : 'Fluoxetine', 
    'Lamotragine' : 'Lamotrigine',
    'Lorazopam' : 'Lorazepam',
    'Lorazapam' : 'Lorazepam',
    'Mirtazapane' : 'Mirtazapine',
    'Mirtazine??' : 'Mirtazapine',
    'Mirtazipine': 'Mirtazapine',
    'Olanzipine': 'Olanzapine', 
    'Beta Blocker (Polpandaol)': 'Propanolol',
    'Pregabalin? (participant put progaviline on the form)' : 'Pregabalin',
    'Propanol' : 'Propanolol',
    'Propropranal' : 'Propanolol',
    'Propanalol' : 'Propanolol',
    'Cantirez pin' : 'other',
    'Sertreline': 'Sertraline',
    'Sertriline': 'Sertraline',
    'Setraline': 'Sertraline',
    'temezepam' : 'Temazepam',
    'Venlaflaxine': 'Venlafaxine',
    'Vendafaxine': 'Venlafaxine',
    'May-27' : 9999
})

type_dict_med = dict({
    'Quetiapine': 'atyp_antipsych',
    'Olanzapine': 'atyp_antipsych',
    'Risperidone': 'atyp_antipsych',
    'Citalopram' : 'SSRI',
    'Sertraline' : 'SSRI',
    'Fluoxetine' : 'SSRI', 
    'Paroxetine' : 'SSRI', 
    'Escitalopram' : 'SSRI', 
    'Venlafaxine': 'SNRI',
    'Doxepin': 'tricyclic',
    'Amitriptyline': 'tricyclic',
    'Mirtazapine' : 'mirtazapin',
    'Lorazepam' : 'BZD',
    'Diazepam' : 'BZD',
    'Temazepam' : 'BZD', 
    'Propranolol' : 'beta blocker',
    'Thyroxine' : 'other type',
    'Pregabalin' : 'other type',
    'Thyroxine' : 'other type',
    'Zopiclone' : 'other type',
    'Zolpidem' : 'other type',
    'Promiphazine' : 'other type',
    'Subutex' : 'other type',
    'Fragmin': 'other type', 
    'Lactulose' : 'other type',
    'Nitrazepam' : 'BZD',
    'different types of drugs - cant remember' : 'other',
    'off medication for 2-3 weeks now': 'off meds',
    'Lamotrigine' : 'anticonvuls',
    'topiramate' : 'anticonvuls'
})

# replace in df
for col in range(5):
    df_fgen[f'Medication{col+1}'] = df_fgen[f'Medication{col+1}'].replace(rename_dict_med).values.copy()
    df_fgen[f'Medication{col+1}_type'] = df_fgen[f'Medication{col+1}'].replace(type_dict_med)
#%%
# add composite scores
for c in [col for col in df_fgen.columns if 'CTQ' in col]:
    df_fgen[c] = df_fgen[c].replace(9999, np.nan)

CTQ_sum = np.nansum(np.array(df_fgen[[c for c in df_fgen.columns if 'CTQ' in c]].astype('f')), axis = 1)
df_fgen['CTQ_sum'] = CTQ_sum

df_fgen['BMI'] = df_fgen['Weight_kg'].values.astype('f')/((df_fgen['Height_cm'].values.astype('f')*0.01)**2)

#%% 
# replace SDI
df_fgen['SocialDeprivationIndex'].replace(9999, np.nan, inplace = True)
#%%
# save
df_fgen.to_csv(f'{pth}/relevant_data_aims13.csv')
# %%
short_colnames =['ID', 'SocialDeprivationIndex', 'Gender', 'Age', 'Referral_Diagnosis', 'CTQ_sum']
df_short = df_fgen[short_colnames].copy()
df_short.to_csv(f'{pth}/relevant_data_short.csv')
# %%
