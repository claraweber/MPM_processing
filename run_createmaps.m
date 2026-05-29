function run_createmaps(sub, ses)

% add spm path
addpath('spm_25.01.02/spm', ...
    genpath('hMRI-toolbox-1.0.0-beta'), ...
    'scripts');

spm_jobman('initcfg');

basepath = '/processing/';

matlabbatch{1}.spm.tools.hmri.hmri_config.hmri_setdef.customised = {[ basepath 'hMRI_toolbox/hMRI-toolbox-1.0.0-beta/config/local/hmri_mpmCNG.m']};
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.output.outdir = {[ basepath 'outputs/hMRI_maps/sub-' sub ]};
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.sensitivity.RF_us = '-';
%%
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.b1_type.i3D_EPI.b1input = {
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-1_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-1_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-2_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-2_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-3_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-3_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-4_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-4_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-5_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-5_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-6_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-6_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-7_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-7_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-8_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B1_angle-8_echo-2_part-mag_MPM.nii,1']
                                                                         };
%%
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.b1_type.i3D_EPI.b0input = {
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B0_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B0_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'BIDS/sub-' sub '/ses-' ses '/fmap/sub-' sub '_ses-' ses '_acq-B0_echo-2_part-phase_MPM.nii,1']
                                                                         };
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.b1_type.i3D_EPI.b1parameters.b1defaults = {[ basepath 'hMRI_toolbox/hMRI-toolbox-1.0.0-beta/config/local/hmri_B1CNG.m' ]};
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.raw_mpm.MT = {
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-3_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-4_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-5_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-MTw_echo-6_part-mag_MPM.nii,1']
                                                           };
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.raw_mpm.PD = {
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-3_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-4_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-5_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-6_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-7_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-PDw_echo-8_part-mag_MPM.nii,1']
                                                             };
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.raw_mpm.T1 = {
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-1_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-2_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-3_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-4_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-5_part-mag_MPM.nii,1']
                                                                         [ basepath 'outputs/denoise/sub-' sub '/Results/LcpcaDenoised_sub-' sub '_ses-' ses '_acq-T1w_echo-6_part-mag_MPM.nii,1']
                                                                         };
matlabbatch{2}.spm.tools.hmri.create_mpm.subj.popup = false;

spm_jobman('run', matlabbatch) 
end