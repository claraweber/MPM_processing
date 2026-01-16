#!/bin/bash
# Run Freesurfer surface conversion on R1 data from hMRI outputs

# set Freesurfer directory
#export SUBJECTS_DIR=/path/to/freesurfer/outputs

SUBJECT="sub-${1}"
mkdir -p $SUBJECTS_DIR/$SUBJECT/mri/orig

# R1 map was copied from hMRI output to BIDS structure
R1_map=/BIDSdir/${SUBJECT}/ses-01/anat/${SUBJECT}_ses-01_run-01_R1_UNICORT.nii.gz 

mri_convert $R1_map $SUBJECTS_DIR/$SUBJECT/mri/orig/001.mgz

# run freesurfer surface construction
recon-all -subjid $SUBJECT -all

# if fail due to lack of wm voxels of intensity 110, set control points in wm (on nu.gz)
# in freeview and re-run this script
