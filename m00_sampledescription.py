"""
Sample description

Clara Weber, MD
June 2026
"""
#%%
# housekeeping
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

# load data - presorted
df = pd.read_csv('../relevant_data_aims13.csv')

#%%
# cleanup operations
df.loc[df['CTQ_sum'] > 28*5, 'CTQ_sum'] = np.nan
#%%
# split in samples
df_bpd = df[df['Referral_Diagnosis'] == 1].copy()
df_aspd = df[df['Referral_Diagnosis'] == 2].copy()
df_crc = df[df['Referral_Diagnosis'] == 3].copy()
df_mdd = df[df['Referral_Diagnosis'] == 4].copy()
# %%
# distribution of diagnoses
np.unique(df['Referral_Diagnosis'], return_counts = True)

# get summary stats
summary = []
names = ['all', 'BPD', 'ASPD', 'MDD', 'CRC']
for s, subgroup in enumerate([df, df_bpd, df_aspd, df_mdd, df_crc]):
    gs = []
    gs.append(names[s])
    gs.append(len(subgroup))
    gs.append(f"{np.mean(subgroup['Age'].values.astype('f')):.3f}±{np.std(subgroup['Age'].values.astype('f')):.3f}")
    gs.append(f"{len(subgroup[subgroup['Gender']==2])*100/len(subgroup):.2f}%")
    gs.append(f"{np.nanmedian(subgroup['CTQ_sum'].values.astype('f'))} [{np.nanmin(subgroup['CTQ_sum'].values.astype('f'))}-{np.nanmax(subgroup['CTQ_sum'].values.astype('f'))}]")
    gs.append(f"{subgroup['CTQ_sum'].isna().sum()*100/len(subgroup):.2f}%")
    gs.append(f"{np.nanmedian(subgroup['SocialDeprivationIndex'].values.astype('f'))} [{np.nanmin(subgroup['SocialDeprivationIndex'].values.astype('f'))}-{np.nanmax(subgroup['CTQ_sum'].values.astype('f'))}]")
    gs.append(f"{subgroup['SocialDeprivationIndex'].isna().sum()*100/len(subgroup):.2f}%")
    summary.append(gs)

pd.DataFrame(summary, columns = ['group', 'n', 'mean±sd age', 'fem', 'median CTQ [range]', 'CTQ nans', 'median SDI [range]', 'SDI nans']).to_csv('demographics.csv')
# %%
# visualize basic demographics
#ax[0].set_xticklabels(['BPD', 'ASPD', 'CRC', 'MDD'])
df['Referral_Diagnosis'].replace({1:'BPD', 2:'ASPD', 3:'CRC', 4:'MDD'}, inplace= True)
df['Referral_Diagnosis'] = pd.Categorical(df['Referral_Diagnosis'], ['BPD','ASPD','MDD','CRC'])
colors = ["#7265a6","#f4cb00", "#28a9a2", "#697272"]

sbn.set_style('white')
fig, ax = plt.subplots(4,1, figsize = (4,6))
sbn.histplot(data = df, x = 'Referral_Diagnosis', hue = 'Referral_Diagnosis', ax = ax[0], multiple = 'stack', palette = colors, legend = False, discrete=True)
ax[0].set_ylabel('% Dx')
ax[0].set_xticks([1,2,3,4])
sbn.histplot(data = df, x = 'Age', hue = 'Referral_Diagnosis', ax = ax[1], alpha = 0.6, multiple = 'stack', palette = colors, legend = False, common_norm=True, kde = True, stat = 'percent', binwidth = 3)
ax[1].set_ylabel('Age by Dx')
sbn.histplot(data = df, x = 'CTQ_sum', hue = 'Referral_Diagnosis', ax = ax[2], alpha = 0.6, multiple = 'stack', palette = colors, legend = False, stat = 'percent', kde = True, common_norm=True, binwidth = 5)
ax[2].set_ylabel(r'$\Sigma$ CTQ by Dx')
sbn.histplot(data = df, x = 'SocialDeprivationIndex', hue = 'Referral_Diagnosis', ax = ax[3], alpha = 0.6, multiple = 'stack', palette = colors, legend = False, stat = 'percent', kde = True, common_norm=True, binwidth = 5)
ax[3].set_ylabel('SDI by Dx')
ax[3].set_xlabel('')
fig.savefig('demographics.svg', bbox_inches = 'tight')
# %%
# medication use
df['n_meds'] = (df[['Medication1', 'Medication2', 'Medication3', 'Medication4', 'Medication5']] != '9999').sum(axis=1)

fig, ax = plt.subplots(figsize = (4,2))
sbn.histplot(data = df, x = 'n_meds', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, shrink = 0.8, legend = False)
fig.savefig('medication.svg', bbox_inches = 'tight')

fig, ax = plt.subplots(1,5, figsize = (7, 4), sharey = True)
sbn.histplot(data = df[df['Medication1_type']!='9999'], y = 'Medication1_type', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, legend = False, ax = ax[0])
ax[0].tick_params(axis='x', labelrotation=90)
sbn.histplot(data = df[df['Medication2_type']!='9999'], y = 'Medication2_type', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, legend = False, ax = ax[1])
ax[1].tick_params(axis='x', labelrotation=90)
sbn.histplot(data = df[df['Medication3_type']!='9999'], y = 'Medication3_type', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, legend = False, ax = ax[2])
ax[2].tick_params(axis='x', labelrotation=90)
sbn.histplot(data = df[df['Medication4_type']!='9999'], y = 'Medication4_type', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, legend = False, ax = ax[3])
ax[3].tick_params(axis='x', labelrotation=90)
sbn.histplot(data = df[df['Medication5_type']!='9999'], y = 'Medication5_type', hue = 'Referral_Diagnosis', alpha = 1, multiple = 'dodge', palette = colors,  common_norm=False, stat = 'percent', discrete = True, legend = False, ax = ax[4])
ax[4].tick_params(axis='x', labelrotation=90)
fig.savefig('medicationtype.svg', bbox_inches = 'tight')
# %%
