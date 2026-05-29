#!/bin/bash
#SBATCH --job-name=mp01createhMRI
#SBATCH --nodes=1
#SBATCH --mem=20G
#SBATCH --cpus-per-task=2
#SBATCH --time=01:29:00
#SBATCH --ntasks=1
#SBATCH --partition=cpu_q
#SBATCH --output=mp02createhMRI_%j.out
#SBATCH --error=mp02createhMRI_%j.err

subj=$1

ses2pth="BIDS/sub-${subj}/ses-02"
ses1pth="BIDS/sub-${subj}/ses-01"

if [ -d "$ses2pth" ]; then
	ses=02
else
	ses=01
fi

matlab -batch "run_createmaps('$subj', '$ses')"