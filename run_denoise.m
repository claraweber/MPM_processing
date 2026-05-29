function run_denoise(sub, ses)

% add spm path
addpath('spm_25.01.02/spm', ...
    genpath('hMRI-toolbox-1.0.0-beta'), ...
    'scripts');

spm_jobman('initcfg');

basepath = 'processing/';

matlabbatch{1}.spm.tools.hmri.hmri_config.hmri_setdef.customised = {[basepath 'hMRI_toolbox/hMRI-toolbox-1.0.0-beta/config/local/hmri_mpmCNG.m' ]};
matlabbatch{2}.spm.tools.hmri.denoise.subj.output.outdir = {[ basepath 'outputs/denoise/sub-' sub ]};
matlabbatch{2}.spm.tools.hmri.denoise.subj.pdw.mag_img = {
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-1_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-2_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-3_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-4_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-5_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-6_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-7_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-PDw_echo-8_part-mag_MPM.nii,1']
                                                          };
matlabbatch{2}.spm.tools.hmri.denoise.subj.pdw.phase_img = '';
matlabbatch{2}.spm.tools.hmri.denoise.subj.t1w.mag_img = {
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-1_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-2_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-3_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-4_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-5_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-T1w_echo-6_part-mag_MPM.nii,1']
                                                          };
matlabbatch{2}.spm.tools.hmri.denoise.subj.t1w.phase_img = '';
matlabbatch{2}.spm.tools.hmri.denoise.subj.mtw.mag_img = {
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-1_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-2_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-3_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-4_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-5_part-mag_MPM.nii,1']
                                                          [ basepath 'BIDS/sub-' sub '/ses-' ses '/anat/sub-' sub '_ses-' ses '_acq-MTw_echo-6_part-mag_MPM.nii,1']
                                                          };
matlabbatch{2}.spm.tools.hmri.denoise.subj.mtw.phase_img = '';
matlabbatch{2}.spm.tools.hmri.denoise.subj.denoisingtype.lcpca_denoise.DNparameters.DNmetadata = 'yes';
matlabbatch{2}.spm.tools.hmri.denoise.subj.denoisingtype.lcpca_denoise.std = 1.05;
matlabbatch{2}.spm.tools.hmri.denoise.subj.denoisingtype.lcpca_denoise.ngbsize = 4;
matlabbatch{2}.spm.tools.hmri.denoise.subj.popup = false;

spm_jobman('run', matlabbatch) 
end