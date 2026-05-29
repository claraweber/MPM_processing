#!/bin/bash
# show hMRI outputs for QC

sub="sub-${1}"
ses2pth="BIDS/${sub}/ses-02"
ses1pth="BIDS/${sub}/ses-01"

if [ -d "$ses2pth" ]; then
	BIDSpath="$ses2pth"
	ses="ses-02"
else
	BIDSpath="$ses1pth"
	ses="ses-01"
fi
# mk tmp dir
mkdir tmp

# convert reoriented scans to test alignment
mri_convert "${BIDSpath}/anat/${sub}_${ses}"*MTsat.nii.gz "tmp/mtsat.mgz"
mri_convert "${BIDSpath}/anat/${sub}_${ses}"*PD.nii.gz "tmp/pd.mgz"
mri_convert "${BIDSpath}/anat/${sub}_${ses}"*R1.nii.gz "tmp/r1.mgz"
mri_convert "${BIDSpath}/anat/${sub}_${ses}"*R2s.nii.gz "tmp/r2.mgz"

# show in freeview
freeview --volume tmp/mtsat.mgz:colormap=grayscale:grayscale=0,2 --volume tmp/pd.mgz:colormap=grayscale:grayscale=50,120 --volume tmp/r1.mgz:colormap=grayscale:grayscale=0,1.4 --volume tmp/r2.mgz:colormap=grayscale:grayscale=0,70 

# rm tmp dir
rm -r tmp