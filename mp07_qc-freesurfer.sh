#!/bin/bash
#SBATCH --job-name=mp07
#SBATCH --nodes=1
#SBATCH --mem=10G
#SBATCH --cpus-per-task=2
#SBATCH --time=13:59:00
#SBATCH --ntasks=1
#SBATCH --partition=cpu_q
#SBATCH --output=mp07_%j.out
#SBATCH --error=mp07_%j.err

export SUBJECTS_DIR=outputs/freesurfer/
SUBJECT="sub-${1}"

recon-all -subjid $SUBJECT -autorecon2-cp -autorecon3