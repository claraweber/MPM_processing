#!/bin/bash
# for each of 10 equivolumetric surfaces, get data at this depth
# uses python helper script - activate respective python env

# set paths
subj="sub-${1}"
export SUBJECTS_DIR="outputs/freesurfer"

ses2pth="BIDS/${subj}/ses-02/anat"
ses1pth="BIDS/${subj}/ses-01/anat"

if [ -d "$ses2pth" ]; then
	MT_map="${ses2pth}/${subj}_ses-02_run-01_MTsat.nii.gz"
	R2_map="${ses2pth}/${subj}_ses-02_run-01_R2s.nii.gz"
else
	MT_map="${ses1pth}/${subj}_ses-01_run-01_MTsat.nii.gz"
	R2_map="${ses1pth}/${subj}_ses-01_run-01_R2s.nii.gz"
fi
outpth="outputs/equivols"

# create tmp directory
mkdir tmp

# convert subject's MTsat to mgz
mri_convert $MT_map "./tmp/${subj}-mt.mgz"
mri_convert $R2_map "./tmp/${subj}-r2.mgz"

for hemi in lh rh; do
	for depth in 0.0 0.07692307692307693 0.15384615384615385 0.23076923076923078 0.3076923076923077 0.38461538461538464 0.46153846153846156 0.5384615384615384 0.6153846153846154 0.6923076923076923 0.7692307692307693 0.8461538461538461  0.9230769230769231 1.0; do
	# sample at surface
	mri_vol2surf --interp trilin --src "./tmp/${subj}-mt.mgz" --out "./tmp/${subj}_${hemi}_${depth}.mgh" --hemi $hemi --surf "equi${depth}.pial" --regheader $subj

	# resample to fsa5
	mri_surf2surf --srcsubject $subj --srcsurfval "./tmp/${subj}_${hemi}_${depth}.mgh" --trgsubject ico --trgicoorder 5 --trgsurfval "${outpth}/${subj}_${depth}_fsa5.${hemi}.mgh" --hemi $hemi 
	
	# R2s
	mri_vol2surf --interp trilin --src "./tmp/${subj}-r2.mgz" --out "./tmp/${subj}_${hemi}_${depth}_r2.mgh" --hemi $hemi --surf "equi${depth}.pial" --regheader $subj

	# resample to fsa5
	mri_surf2surf --srcsubject $subj --srcsurfval "./tmp/${subj}_${hemi}_${depth}_r2.mgh" --trgsubject ico --trgicoorder 5 --trgsurfval "${outpth}/${subj}_${depth}_r2_fsa5.${hemi}.mgh" --hemi $hemi 
	done
done

# clear tmp directory
rm -r tmp

# get all data for subject in the same df
python mp09_helper_aggregate.py ${1}

# clean up all intermediate files
rm "${outpth}/${subj}"*_fsa5.lh.mgh
rm "${outpth}/${subj}"*_fsa5.rh.mgh
rm -r "outputs/denoise/${subj}"
rm "outputs/t1_coregs/${subj}"*
rm -r "/MPM_dicoms/${subj}"