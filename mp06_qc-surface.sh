#!/bin/bash
# Load surfs into freeview for QC
# do manual surface corrections with control points and brainmask edits

subj=$1
datadir="outputs/freesurfer"

ses2pth="BIDS/sub-${subj}/ses-02"
ses1pth="BIDS/sub-${subj}/ses-01"

if [ -d "$ses2pth" ]; then
	BIDSpath="$ses2pth/anat"
	ses="ses-02"
else
	BIDSpath="$ses1pth/anat"
	ses="ses-01"
fi

mkdir tmp
mri_convert "${BIDSpath}/sub-${subj}_${ses}_run-01_MTsat.nii.gz" "tmp/sub-${subj}_mt.mgz"

freeview -v ${datadir}/sub-${subj}/mri/brainmask.mgz \
-v ${datadir}/sub-${subj}/mri/orig/001.mgz \
-v "tmp/sub-${subj}_mt.mgz":colormap=grayscale:grayscale=0,2 \
-f ${datadir}/sub-${subj}/surf/lh.white:edgecolor=yellow \
${datadir}/sub-${subj}/surf/lh.pial:edgecolor=red \
${datadir}/sub-${subj}/surf/rh.white:edgecolor=yellow \
${datadir}/sub-${subj}/surf/rh.pial:edgecolor=red 

rm -r tmp