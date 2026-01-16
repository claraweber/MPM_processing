#!/bin/bash
# generate equivolumetric surfaces based on freesurfer output
# using github.com/kwagstyl/surface_tools

datadir=$2
subj="sub-${1}"

export SUBJECTS_DIR=$datadir

# left hemisphere
generate_equivolumetric_surfaces --smoothing 0 \
  ${datadir}/${subj}/surf/lh.pial \
  ${datadir}/${subj}/surf/lh.white \
  10 \
  lh.equi \
  --software freesurfer --subject_id ${subj}

# right hemisphere
generate_equivolumetric_surfaces --smoothing 0 \
  ${datadir}/${subj}/surf/rh.pial \
  ${datadir}/${subj}/surf/rh.white \
  10 \
  rh.equi \
  --software freesurfer --subject_id ${subj}

# get data at a certain surface
mri_vol2surf --mov $MT_map \ 
  --ref orig/001.mgz \
  --hemi lh \ 
  --surf equi0.3333333333333333.pial \
  --regheader $subj \
  --o “${datadir}/layerdata/${subj}-lh_equi-0.3.mgh"
