#!/bin/bash
# move hMRI outcomes to BIDS structure

subj=$1
echo $subj

mpmpath="outputs/hMRI_maps/sub-${subj}/Results"

ses2pth="BIDS/sub-${subj}/ses-02"
ses1pth="BIDS/sub-${subj}/ses-01"

if [ -d "$ses2pth" ]; then
	BIDSpath="$ses2pth/anat"
	ses="ses-02"
else
	BIDSpath="$ses1pth/anat"
	ses="ses-01"
fi

cp "${mpmpath}/"*R1.json "${BIDSpath}/sub-${subj}_${ses}_run-01_R1.json";
cp "${mpmpath}/"*R1.nii "${BIDSpath}/sub-${subj}_${ses}_run-01_R1.nii";

cp "${mpmpath}/"*PD.json "${BIDSpath}/sub-${subj}_${ses}_run-01_PD.json";
cp "${mpmpath}/"*PD.nii "${BIDSpath}/sub-${subj}_${ses}_run-01_PD.nii";

cp "${mpmpath}/"*R2s*.json "${BIDSpath}/sub-${subj}_${ses}_run-01_R2s.json";
cp "${mpmpath}/"*R2s*.nii "${BIDSpath}/sub-${subj}_${ses}_run-01_R2s.nii";

cp "${mpmpath}/"*MTsat.json "${BIDSpath}/sub-${subj}_${ses}_run-01_MTsat.json";
cp "${mpmpath}/"*MTsat.nii "${BIDSpath}/sub-${subj}_${ses}_run-01_MTsat.nii";

gzip "${BIDSpath}/"*.nii