#!/bin/bash
#SBATCH --job-name=mp05
#SBATCH --nodes=1
#SBATCH --mem=10G
#SBATCH --cpus-per-task=2
#SBATCH --time=15:59:00
#SBATCH --ntasks=1
#SBATCH --partition=cpu_q
#SBATCH --output=mp05_%j.out
#SBATCH --error=mp05_%j.err

module load FSL/6.0.5.1-foss-2021a
export SUBJECTS_DIR=/outputs/freesurfer/

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

native_T1="${BIDSpath}/anat/${sub}_${ses}_acq-T1w_echo-1_part-mag_MPM.nii"
PDw_ref="${BIDSpath}/anat/${sub}_${ses}_run-01_PD.nii.gz"

reft1pth="outputs/t1_coregs"

flirt -in $native_T1 -ref $PDw_ref -o "${reft1pth}/${sub}-coreg_ref.nii.gz"

mkdir "${SUBJECTS_DIR}/${sub}"
mkdir "${SUBJECTS_DIR}/${sub}/mri"
mkdir "${SUBJECTS_DIR}/${sub}/mri/orig"

mri_convert "${reft1pth}/${sub}-coreg_ref.nii.gz" "${SUBJECTS_DIR}/${sub}/mri/orig/001.mgz"

recon-all -subjid $sub -all