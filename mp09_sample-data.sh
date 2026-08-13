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

# create tmp_${subj} directory
mkdir "tmp_${subj}"

# get mri ribbon
mri_convert "${SUBJECTS_DIR}/${subj}/mri/aseg.mgz" "tmp_${subj}/aseg.nii.gz"
fslmaths "tmp_${subj}/aseg.nii.gz" -thr 3 -uthr 3 -bin "tmp_${subj}/lhctx.nii.gz"
fslmaths "tmp_${subj}/aseg.nii.gz" -thr 42 -uthr 42 -bin "tmp_${subj}/rhctx.nii.gz"
fslmaths "tmp_${subj}/lhctx.nii.gz" -add "tmp_${subj}/rhctx.nii.gz" -bin "tmp_${subj}/maskctx.nii.gz"
mri_convert "tmp_${subj}/maskctx.nii.gz" "tmp_${subj}/mask.mgz"

# convert subject's MTsat to mgz
mri_convert $MT_map "./tmp_${subj}/${subj}-mt_full.mgz"
mri_convert $R2_map "./tmp_${subj}/${subj}-r2_full.mgz"

mri_mask "./tmp_${subj}/${subj}-mt_full.mgz" "./tmp_${subj}/mask.mgz" "./tmp_${subj}/${subj}-mt.mgz"
mri_mask "./tmp_${subj}/${subj}-r2_full.mgz" "./tmp_${subj}/mask.mgz" "./tmp_${subj}/${subj}-r2.mgz"

for hemi in lh rh; do
	for depth in 0.0 0.07692307692307693 0.15384615384615385 0.23076923076923078 0.3076923076923077 0.38461538461538464 0.46153846153846156 0.5384615384615384 0.6153846153846154 0.6923076923076923 0.7692307692307693 0.8461538461538461  0.9230769230769231 1.0; do
	# sample at surface
	mri_vol2surf --interp trilin --src "./tmp_${subj}/${subj}-mt.mgz" --out "./tmp_${subj}/${subj}_${hemi}_${depth}.mgh" --hemi $hemi --surf "equi${depth}.pial" --regheader $subj

	# resample to fsa5
	mri_surf2surf --srcsubject $subj --srcsurfval "./tmp_${subj}/${subj}_${hemi}_${depth}.mgh" --trgsubject ico --trgicoorder 5 --trgsurfval "${outpth}/${subj}_${depth}_fsa5.${hemi}.mgh" --hemi $hemi #--nsmooth-out 5
	
	# R2s
	mri_vol2surf --interp trilin --src "./tmp_${subj}/${subj}-r2.mgz" --out "./tmp_${subj}/${subj}_${hemi}_${depth}_r2.mgh" --hemi $hemi --surf "equi${depth}.pial" --regheader $subj

	# resample to fsa5
	mri_surf2surf --srcsubject $subj --srcsurfval "./tmp/${subj}_${hemi}_${depth}_r2.mgh" --trgsubject ico --trgicoorder 5 --trgsurfval "${outpth}/${subj}_${depth}_r2_fsa5.${hemi}.mgh" --hemi $hemi #--nsmoothout 5
	done
done

# clear tmp_${subj} directory
rm -r tmp_${subj}

# get all data for subject in the same df
python mp09_helper_aggregate.py ${1}

# clean up all intermediate files
rm "${outpth}/${subj}"*_fsa5.lh.mgh
rm "${outpth}/${subj}"*_fsa5.rh.mgh
rm -r "outputs/denoise/${subj}"
rm "outputs/t1_coregs/${subj}"*
rm -r "/MPM_dicoms/${subj}"
