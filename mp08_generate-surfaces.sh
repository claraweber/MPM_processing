#!/bin/bash
# create equivolumetric surfaces
# using tool by Konrad Wagstyl - shoutout to his github kwagstyl
# installed in conda environment, activate before running
# 14 surfaces, see Paquola 2019 and 2026

datadir='outputs/freesurfer'
SUBJECT="sub-${1}"
export SUBJECTS_DIR=$datadir

# left hemisphere
generate_equivolumetric_surfaces --smoothing 0 ${datadir}/${SUBJECT}/surf/lh.pial ${datadir}/${SUBJECT}/surf/lh.white 14 lh.equi --software freesurfer --subject_id ${SUBJECT}

# right hemisphere
generate_equivolumetric_surfaces --smoothing 0 ${datadir}/${SUBJECT}/surf/rh.pial ${datadir}/${SUBJECT}/surf/rh.white 14 rh.equi --software freesurfer --subject_id ${SUBJECT}

