%-----------------------------------------------------------------------
% Matlab/SPM script to process one case in hMRI toolbox
% here using UNICORT for B1 correction
%-----------------------------------------------------------------------
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.output.indir = 'yes';
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.sensitivity.RF_us = '-';
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.b1_type.UNICORT.b1parameters.b1defaults = {'./hMRI-toolbox-0.6.1/config/local/hmri_b1_local_defaults.m'};
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.raw_mpm.MT = {cellstr(spm_select('ExtFPList', './sub-000', '^mt_.*_e.*\.nii$'))};
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.raw_mpm.PD = {cellstr(spm_select('ExtFPList', './sub-000', '^pd_.*_e.*\.nii$'))};
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.raw_mpm.T1 = {cellstr(spm_select('ExtFPList', './sub-000', '^t1_.*_e.*\.nii$'))};
matlabbatch{1}.spm.tools.hmri.create_mpm.subj.popup = false;
