#%%
import numpy as np
import pandas as pd

# ── Item lists per subscale (from R script) ──────────────────────────────────

subscale_items = {
    # AFI — note: AFI_1 and AFI_3 items are reverse-scored in R (6-x)
    'AFI_Au':  ['AFI_1_1', 'AFI_1_2', 'AFI_1_3', 'AFI_1_4', 'AFI_1_5'],   # reversed
    'AFI_IT':  ['AFI_3_1', 'AFI_3_2', 'AFI_3_3', 'AFI_3_4', 'AFI_3_5'],   # reversed
    'AFI_SC':  ['AFI_2_1', 'AFI_2_2', 'AFI_2_3', 'AFI_2_4', 'AFI_2_5'],   # not reversed

    # APSD
    'APSD_CU': ['APSD3', 'APSD7', 'APSD12', 'APSD18', 'APSD19', 'APSD20'],  # 3,7,12,18,20 reversed (2-x)
    'APSD_IM': ['APSD1', 'APSD4', 'APSD9', 'APSD13', 'APSD17'],
    'APSD_NA': ['APSD5', 'APSD8', 'APSD10', 'APSD11', 'APSD14', 'APSD15', 'APSD16'],

    # BIS-11
    'BIS_CI':  ['BIS5', 'BIS9', 'BIS11', 'BIS20', 'BIS28', 'BIS6', 'BIS24', 'BIS26'],  # BIS9, BIS20 reversed (5-x)
    'BIS_MI':  ['BIS2', 'BIS3', 'BIS4', 'BIS17', 'BIS19', 'BIS22', 'BIS25', 'BIS16', 'BIS21', 'BIS23', 'BIS30'],  # BIS4, BIS30 reversed
    'BIS_NPI': ['BIS1', 'BIS7', 'BIS8', 'BIS12', 'BIS13', 'BIS14', 'BIS10', 'BIS15', 'BIS18', 'BIS27', 'BIS29'],  # BIS1,7,8,12,13,10,15,29 reversed

    # BSI
    'Anxiety':    ['BSI1', 'BSI12', 'BSI19', 'BSI38', 'BSI45', 'BSI49'],
    'Depression': ['BSI9', 'BSI16', 'BSI17', 'BSI18', 'BSI35', 'BSI50'],
    'Hostility':  ['BSI6', 'BSI13', 'BSI40', 'BSI41', 'BSI46'],
    'Interpers':  ['BSI20', 'BSI21', 'BSI22', 'BSI42'],
    'OC':         ['BSI5', 'BSI15', 'BSI26', 'BSI27', 'BSI32', 'BSI36'],
    'Paranoia':   ['BSI4', 'BSI10', 'BSI24', 'BSI48', 'BSI51'],
    'Phobia':     ['BSI8', 'BSI28', 'BSI31', 'BSI43', 'BSI47'],
    'Psychot':    ['BSI3', 'BSI14', 'BSI34', 'BSI44', 'BSI53'],
    'Somat':      ['BSI2', 'BSI7', 'BSI23', 'BSI29', 'BSI30', 'BSI33', 'BSI37'],

    # DASI
    'DASI_DA': ['DASI1', 'DASI2', 'DASI3', 'DASI4', 'DASI5', 'DASI6', 'DASI8', 'DASI11', 'DASI12'],
    'DASI_SH': ['DASI9', 'DASI10'],

    # DERS  (individual items reversed within R before mean)
    'DERS_st':    ['DERS15', 'DERS16', 'DERS22', 'DERS28', 'DERS30', 'DERS31', 'DERS35', 'DERS36'],  # DERS22 reversed (6-x)
    'DERS_aw':    ['DERS2', 'DERS6', 'DERS8', 'DERS10', 'DERS17', 'DERS34'],   # all reversed (6-x)
    'DERS_cl':    ['DERS1', 'DERS4', 'DERS5', 'DERS7', 'DERS9'],               # DERS1, DERS7 reversed
    'DERS_goals': ['DERS13', 'DERS18', 'DERS20', 'DERS26', 'DERS33'],          # DERS20 reversed
    'DERS_im':    ['DERS3', 'DERS14', 'DERS19', 'DERS24', 'DERS27', 'DERS32'], # DERS24 reversed
    'DERS_nona':  ['DERS11', 'DERS12', 'DERS21', 'DERS23', 'DERS25', 'DERS29'],

    # DES
    'DES_Ab': ['DES2', 'DES14', 'DES15', 'DES17', 'DES18', 'DES20'],
    'DES_Am': ['DES3', 'DES4', 'DES5', 'DES8', 'DES25', 'DES26'],
    'DES_De': ['DES7', 'DES11', 'DES12', 'DES13', 'DES27', 'DES28'],

    # ECR-R  (multiple items reversed, 8-x)
    'ECRRANX':  ['ECRR1', 'ECRR4', 'ECRR5', 'ECRR6', 'ECRR10', 'ECRR11',
                 'ECRR12', 'ECRR13', 'ECRR14', 'ECRR18', 'ECRR21', 'ECRR24',
                 'ECRR26', 'ECRR29', 'ECRR30', 'ECRR31', 'ECRR33', 'ECRR35'],  # ECRR5, ECRR31 reversed
    'ECRRAVOI': ['ECRR2', 'ECRR3', 'ECRR7', 'ECRR8', 'ECRR9', 'ECRR15',
                 'ECRR16', 'ECRR17', 'ECRR19', 'ECRR20', 'ECRR22', 'ECRR23',
                 'ECRR25', 'ECRR27', 'ECRR28', 'ECRR32', 'ECRR34', 'ECRR36'],  # many reversed

    # EQ  (multiple items reversed, 3-x)
    'EQ_cognitive':            ['eq_1', 'eq_11', 'eq_14', 'eq_15', 'eq_25', 'eq_26', 'eq_29', 'eq_34', 'eq_35', 'eq_36', 'eq_38'],  # all reversed
    'EQ_emotional_reactivity': ['eq_3', 'eq_12', 'eq_16', 'eq_19', 'eq_27', 'eq_31', 'eq_33', 'eq_39'],  # eq_3, eq_27, eq_39 reversed
    'EQ_social_skills':        ['eq_2', 'eq_4', 'eq_7', 'eq_8', 'eq_21', 'eq_37'],  # eq_21, eq_37 reversed

    # GPTS
    'GPTSPers': ['GPTS_B1', 'GPTS_B2', 'GPTS_B3', 'GPTS_B4', 'GPTS_B5', 'GPTS_B6',
                 'GPTS_B7', 'GPTS_B8', 'GPTS_B9', 'GPTS_B10', 'GPTS_B11', 'GPTS_B12',
                 'GPTS_B13', 'GPTS_B14', 'GPTS_B15', 'GPTS_B16'],
    'GPTSsRef': ['GPTS_A1', 'GPTS_A2', 'GPTS_A3', 'GPTS_A4', 'GPTS_A5', 'GPTS_A6',
                 'GPTS_A7', 'GPTS_A8', 'GPTS_A9', 'GPTS_A10', 'GPTS_A11', 'GPTS_A12',
                 'GPTS_A13', 'GPTS_A14', 'GPTS_A15', 'GPTS_A16'],

    # IIP-32  (your columns use IIP3211-style for octant 1, IIP32221-style for octant 2)
    'IIP32_de': ['IIP32110', 'IIP32111', 'IIP32113', 'IIP32115'],           # Cold
    'IIP32_pa': ['IIP32222', 'IIP32225', 'IIP32228', 'IIP32230'],           # Domineering
    'IIP32_no': ['IIP3213', 'IIP32221', 'IIP32224', 'IIP32229'],            # Intrusive
    'IIP32_hi': ['IIP3214', 'IIP3216', 'IIP3217', 'IIP32112'],              # Nonassertive
    'IIP32_jk': ['IIP3211', 'IIP3218', 'IIP32120', 'IIP32231'],             # Overly accommodating
    'IIP32_lm': ['IIP32223', 'IIP32226', 'IIP32227', 'IIP32232'],           # Self-sacrificing
    'IIP32_fg': ['IIP3212', 'IIP3215', 'IIP3219', 'IIP32119'],              # Socially inhibited
    'IIP32_bc': ['IIP32114', 'IIP32116', 'IIP32117', 'IIP32118'],           # Vindictive

    # LHA
    'LHA_agg':  ['LHA1', 'LHA2', 'LHA3', 'LHA4', 'LHA5'],
    'LHA_anti': ['LHA7', 'LHA8', 'LHA9', 'LHA10'],
    'LHA_self': ['LHA6a', 'LHA6b'],   # note: your column is LHA6a not LHA6A

    # OAS
    'OAS_emptiess':  ['OAS17', 'OAS16', 'OAS18', 'OAS15'],
    'OAS_inferior':  ['OAS5', 'OAS2', 'OAS1', 'OAS6', 'OAS4', 'OAS7', 'OAS8'],
    'OAS_reactions': ['OAS12', 'OAS14', 'OAS13', 'OAS9', 'OAS3', 'OAS11'],

    # OPD-SQ  (OPD12, OPD25, OPD36, OPD38, OPD47, OPD55, OPD62, OPD72 reversed 4-x globally)
    'OPDSQ_accepting_help_f':    ['OPD77', 'OPD47', 'OPD12', 'OPD28'],
    'OPDSQ_affect_diff_f':       ['OPD8', 'OPD41', 'OPD51', 'OPD33'],
    'OPDSQ_aff_toler_f':         ['OPD44', 'OPD4', 'OPD70', 'OPD73', 'OPD92'],
    'OPDSQ_anticipat_f':         ['OPD7', 'OPD49', 'OPD85', 'OPD65', 'OPD10', 'OPD63'],
    'OPDSQ_balanc_inc_f':        ['OPD95', 'OPD23', 'OPD87', 'OPD43', 'OPD54', 'OPD6'],
    'OPDSQ_comm_affect_f':       ['OPD31', 'OPD53', 'OPD75', 'OPD61', 'OPD26', 'OPD81'],
    'OPDSQ_trouble_detaching_f': ['OPD14', 'OPD9', 'OPD5', 'OPD82'],
    'OPDSQ_empathy_f':           ['OPD46', 'OPD83', 'OPD35', 'OPD20'],
    'OPDSQ_est_contact_f':       ['OPD79', 'OPD11', 'OPD93', 'OPD72'],
    'OPDSQ_exp_affect_f':        ['OPD86', 'OPD16', 'OPD59', 'OPD22'],
    'OPDSQ_holistic_obj_f':      ['OPD24', 'OPD84', 'OPD60', 'OPD15'],
    'OPDSQ_imp_control_f':       ['OPD19', 'OPD36', 'OPD42', 'OPD2'],
    'OPDSQ_internalization_f':   ['OPD32', 'OPD90', 'OPD45', 'OPD66'],
    'OPDSQ_bodily_self_f':       ['OPD64', 'OPD58', 'OPD37', 'OPD69'],
    'OPDSQ_realistic_obj_f':     ['OPD94', 'OPD78', 'OPD56', 'OPD68', 'OPD17', 'OPD91'],
    'OPDSQ_reg_self_est_f':      ['OPD38', 'OPD40', 'OPD80', 'OPD13'],
    'OPDSQ_self_obj_diff_f':     ['OPD21', 'OPD71', 'OPD18', 'OPD34', 'OPD89', 'OPD50', 'OPD29'],
    'OPDSQ_selfperc_f':          ['OPD1', 'OPD67', 'OPD27', 'OPD48'],
    'OPDSQ_sense_of_identity_f': ['OPD3', 'OPD74', 'OPD52', 'OPD39'],
    'OPDSQ_use_introjects_f':    ['OPD76', 'OPD30', 'OPD57', 'OPD88'],
    'OPDSQ_use_phantasy_f':      ['OPD62', 'OPD55', 'OPD25'],

    # PAI-BOR  (PAI12, PAI14, PAI19, PAI7, PAI20, PAI24 reversed 3-x)
    'PAIBOR_inst': ['PAI1', 'PAI4', 'PAI7', 'PAI10', 'PAI14', 'PAI18'],
    'PAIBOR_ide':  ['PAI2', 'PAI5', 'PAI8', 'PAI11', 'PAI15', 'PAI19'],
    'PAIBOR_rela': ['PAI3', 'PAI6', 'PAI9', 'PAI12', 'PAI16', 'PAI20'],
    'PAIBOR_harm': ['PAI13', 'PAI17', 'PAI21', 'PAI22', 'PAI23', 'PAI24'],

    # PAI-ANT  (your columns: PAIS_AS not PAISAS)
    'PAIANT_atso': ['PAIS_AS1', 'PAIS_AS4', 'PAIS_AS7', 'PAIS_AS10',
                    'PAIS_AS13', 'PAIS_AS16', 'PAIS_AS19', 'PAIS_AS22'],
    'PAIANT_egoc': ['PAIS_AS2', 'PAIS_AS5', 'PAIS_AS8', 'PAIS_AS11',
                    'PAIS_AS14', 'PAIS_AS17', 'PAIS_AS20', 'PAIS_AS23'],
    'PAIANT_sens': ['PAIS_AS3', 'PAIS_AS6', 'PAIS_AS9', 'PAIS_AS12',
                    'PAIS_AS15', 'PAIS_AS18', 'PAIS_AS21', 'PAIS_AS24'],

    # PCL-C  (your columns: PLCS not PCLS)
    'PCLS_avo': ['PLCS10', 'PLCS9', 'PLCS11', 'PLCS12', 'PLCS7', 'PLCS8', 'PLCS6'],
    'PCLS_aro': ['PLCS13', 'PLCS14', 'PLCS15', 'PLCS16', 'PLCS17'],
    'PCLS_re':  ['PLCS1', 'PLCS4', 'PLCS2', 'PLCS3', 'PLCS5'],

    # RFQ-18  (your columns: RQF54_N; several items reversed 8-x)
    'RFQ_other': ['RQF54_1', 'RQF54_2', 'RQF54_6', 'RQF54_7', 'RQF54_14',
                  'RQF54_18', 'RQF54_26', 'RQF54_27', 'RQF54_38'],  # RQF54_2,7,14,27,38 reversed
    'RFQ_self':  ['RQF54_8', 'RQF54_12', 'RQF54_16', 'RQF54_20', 'RQF54_28',
                  'RQF54_35', 'RQF54_40', 'RQF54_45', 'RQF54_46'],  # RQF54_8,35,45,46 reversed

    # SAPAS  (your columns: SAPASadult not SAP)
    'SAPAS': ['SAPASadult1', 'SAPASadult2', 'SAPASadult3', 'SAPASadult4',
              'SAPASadult5', 'SAPASadult6', 'SAPASadult7', 'SAPASadult8'],

    # SPQ
    'SPQ_mistru': ['SPQ63', 'SPQ53', 'SPQ9', 'SPQ60', 'SPQ59', 'SPQ45',
                   'SPQ27', 'SPQ19', 'SPQ18', 'SPQ65', 'SPQ10', 'SPQ44', 'SPQ52'],
    'SPQ_oddity': ['SPQ23', 'SPQ70', 'SPQ32', 'SPQ67', 'SPQ14', 'SPQ5',
                   'SPQ58', 'SPQ34', 'SPQ50', 'SPQ16', 'SPQ7', 'SPQ8', 'SPQ25', 'SPQ61'],
    'SPQ_socanh': ['SPQ62', 'SPQ26', 'SPQ35', 'SPQ66', 'SPQ74', 'SPQ41',
                   'SPQ6', 'SPQ48', 'SPQ33', 'SPQ42', 'SPQ49', 'SPQ72', 'SPQ36', 'SPQ31', 'SPQ43'],
    'SPQ_socanx': ['SPQ71', 'SPQ46', 'SPQ38', 'SPQ29', 'SPQ24', 'SPQ11',
                   'SPQ57', 'SPQ2', 'SPQ51', 'SPQ54', 'SPQ15', 'SPQ73', 'SPQ17',
                   'SPQ69', 'SPQ68', 'SPQ20', 'SPQ4'],
    'SPQ_unusua': ['SPQ12', 'SPQ30', 'SPQ55', 'SPQ40', 'SPQ47', 'SPQ13',
                   'SPQ37', 'SPQ39', 'SPQ21', 'SPQ28', 'SPQ56', 'SPQ3', 'SPQ22', 'SPQ64', 'SPQ1'],

    # SRPS  (SRPS22,24,25,26 reversed 6-x)
    'SRPS_antisocial': ['SRPS2', 'SRPS10', 'SRPS16', 'SRPS18', 'SRPS4'],
    'SRPS_callous':    ['SRPS24', 'SRPS22', 'SRPS25', 'SRPS26'],   # all reversed
    'SRPS_egocentric': ['SRPS5', 'SRPS3', 'SRPS7', 'SRPS13', 'SRPS1',
                        'SRPS17', 'SRPS9', 'SRPS21', 'SRPS23', 'SRPS11'],
}

# ── Rename dictionary: subscale variable name → Table S1 label ───────────────

rename_dict = {
    'AFI_Au':  'AFI Authorship',
    'AFI_IT':  'AFI Interest-taking',
    'AFI_SC':  'AFI Susceptibility to control',
    'APSD_CU': 'APSD Callousness',
    'APSD_IM': 'APSD Impulsiveness',
    'APSD_NA': 'APSD Narcissism',
    'BIS_CI':  'BIS-11 Attentional impulsiveness',
    'BIS_MI':  'BIS-11 Motor impulsiveness',
    'BIS_NPI': 'BIS-11 Non-planning impulsiveness',
    'Anxiety':    'BSI Anxiety',
    'Depression': 'BSI Depression',
    'Hostility':  'BSI Hostility',
    'Interpers':  'BSI Interpersonal sensitivity',
    'OC':         'BSI Obsessive-compulsive',
    'Paranoia':   'BSI Paranoid ideation',
    'Phobia':     'BSI Phobia',
    'Psychot':    'BSI Psychoticism',
    'Somat':      'BSI Somatoform',
    'DASI_DA': 'DASI Drugs and alcohol',
    'DASI_SH': 'DASI Self-harm',
    'DERS_st':    'DERS Emotion-regulation strategies',
    'DERS_aw':    'DERS Emotional awareness',
    'DERS_cl':    'DERS Emotional clarity',
    'DERS_goals': 'DERS Goal-directed behavior',
    'DERS_im':    'DERS Impulse control',
    'DERS_nona':  'DERS Nonacceptance of emotions',
    'DES_Ab': 'DES Absorption',
    'DES_Am': 'DES Amnestic dissociation',
    'DES_De': 'DES Depersonalization',
    'ECRRANX':  'ECR-R Attachment anxiety',
    'ECRRAVOI': 'ECR-R Attachment avoidance',
    'EQ_cognitive':            'EQ Cognitive empathy',
    'EQ_emotional_reactivity': 'EQ Emotional reactivity',
    'EQ_social_skills':        'EQ Social skills',
    'GPTSPers': 'GPTS Feelings of persecution',
    'GPTSsRef': 'GPTS Thoughts of social referencing',
    'IIP32_bc': 'IIP-32 Vindictive',
    'IIP32_de': 'IIP-32 Cold',
    'IIP32_fg': 'IIP-32 Socially inhibited',
    'IIP32_hi': 'IIP-32 Nonassertive',
    'IIP32_jk': 'IIP-32 Overly accomodating',
    'IIP32_lm': 'IIP-32 Self-sacrificing',
    'IIP32_no': 'IIP-32 Intrusive',
    'IIP32_pa': 'IIP-32 Domineering',
    'LHA_agg':  'LHA Aggression',
    'LHA_anti': 'LHA Antisocial behavior',
    'LHA_self': 'LHA Self-directed aggression',
    'OAS_emptiess':  'OAS Feelings of emptiness',
    'OAS_inferior':  'OAS Feelings of inferiority',
    'OAS_reactions': 'OAS Reactions of others',
    'OPDSQ_accepting_help_f':    'OPD-SQ Accepting help',
    'OPDSQ_affect_diff_f':       'OPD-SQ Affect differentiation',
    'OPDSQ_aff_toler_f':         'OPD-SQ Affect tolerance',
    'OPDSQ_anticipat_f':         'OPD-SQ Anticipation',
    'OPDSQ_balanc_inc_f':        'OPD-SQ Balancing interests',
    'OPDSQ_bodily_self_f':       'OPD-SQ Perceiving bodily self',
    'OPDSQ_comm_affect_f':       'OPD-SQ Communicating affect',
    'OPDSQ_empathy_f':           'OPD-SQ Empathy',
    'OPDSQ_est_contact_f':       'OPD-SQ Establishing contact',
    'OPDSQ_exp_affect_f':        'OPD-SQ Experiencing affect',
    'OPDSQ_holistic_obj_f':      'OPD-SQ Holistic object perception',
    'OPDSQ_imp_control_f':       'OPD-SQ Impulse Control',
    'OPDSQ_internalization_f':   'OPD-SQ Internalization',
    'OPDSQ_realistic_obj_f':     'OPD-SQ Realistic object perception',
    'OPDSQ_reg_self_est_f':      'OPD-SQ Regulation of self-esteem',
    'OPDSQ_self_obj_diff_f':     'OPD-SQ Self-object differentiation',
    'OPDSQ_selfperc_f':          'OPD-SQ Self-perception',
    'OPDSQ_sense_of_identity_f': 'OPD-SQ Sense of identity',
    'OPDSQ_trouble_detaching_f': 'OPD-SQ Detaching relationships',
    'OPDSQ_use_introjects_f':    'OPD-SQ Use of introjects',
    'OPDSQ_use_phantasy_f':      'OPD-SQ Use of phantasy',
    'PAIBOR_inst': 'PAI-BOR Affective instability',
    'PAIBOR_ide':  'PAI-BOR Identity problems',
    'PAIBOR_rela': 'PAI-BOR Negative relationships',
    'PAIBOR_harm': 'PAI-BOR Self-harm',
    'PAIANT_atso': 'PAI-ANT Antisociality',
    'PAIANT_egoc': 'PAI-ANT Egocentricity',
    'PAIANT_sens': 'PAI-ANT Sensation-seeking',
    'PCLS_avo': 'PCL-C Avoidance',
    'PCLS_aro': 'PCL-C Hyperarousal',
    'PCLS_re':  'PCL-C Re-experiencing',
    'RFQ_other': 'RFQ-18 Mentalizing of others',
    'RFQ_self':  'RFQ-18 Mentalizing of self',
    'SAPAS': 'SAPAS Personality pathology',
    'SPQ_mistru': 'SPQ Mistrust',
    'SPQ_oddity': 'SPQ Oddity',
    'SPQ_socanh': 'SPQ Social anhedonia',
    'SPQ_socanx': 'SPQ Social anxiety',
    'SPQ_unusua': 'SPQ Unusual beliefs',
    'SRPS_antisocial': 'SRPS Antisociality',
    'SRPS_callous':    'SRPS Callousness',
    'SRPS_egocentric': 'SRPS Egocentricity',
}

# ── Reverse-score specifications (max_val - x) ───────────────────────────────

reverse_specs = {
    # AFI (max=5, so 6-x)
    'AFI_1_1': 5, 'AFI_1_2': 5, 'AFI_1_3': 5, 'AFI_1_4': 5, 'AFI_1_5': 5,
    'AFI_3_1': 5, 'AFI_3_2': 5, 'AFI_3_3': 5, 'AFI_3_4': 5, 'AFI_3_5': 5,
    # APSD (max=2, so 2-x)
    'APSD3': 2, 'APSD7': 2, 'APSD12': 2, 'APSD18': 2, 'APSD20': 2,
    # BIS-11 (max=4, so 5-x)
    'BIS9': 4, 'BIS20': 4, 'BIS4': 4, 'BIS30': 4,
    'BIS1': 4, 'BIS7': 4, 'BIS8': 4, 'BIS12': 4,
    'BIS13': 4, 'BIS10': 4, 'BIS15': 4, 'BIS29': 4,
    # DERS (max=5, so 6-x)
    'DERS22': 5, 'DERS2': 5, 'DERS6': 5, 'DERS8': 5, 'DERS10': 5,
    'DERS17': 5, 'DERS34': 5, 'DERS1': 5, 'DERS7': 5, 'DERS20': 5, 'DERS24': 5,
    # ECR-R (max=7, so 8-x)
    'ECRR5': 7, 'ECRR31': 7,
    'ECRR2': 7, 'ECRR3': 7, 'ECRR9': 7, 'ECRR15': 7,
    'ECRR17': 7, 'ECRR20': 7, 'ECRR23': 7, 'ECRR25': 7,
    'ECRR28': 7, 'ECRR32': 7, 'ECRR34': 7, 'ECRR36': 7,
    # EQ (max=3, so 3-x)
    'eq_1': 3, 'eq_11': 3, 'eq_14': 3, 'eq_15': 3, 'eq_25': 3,
    'eq_26': 3, 'eq_29': 3, 'eq_34': 3, 'eq_35': 3, 'eq_36': 3, 'eq_38': 3,
    'eq_3': 3, 'eq_27': 3, 'eq_39': 3,
    'eq_21': 3, 'eq_37': 3,
    # OPD-SQ (max=4, so 4-x)
    'OPD12': 4, 'OPD25': 4, 'OPD36': 4, 'OPD38': 4,
    'OPD47': 4, 'OPD55': 4, 'OPD62': 4, 'OPD72': 4,
    # PAI-BOR (max=3, so 3-x)
    'PAI12': 3, 'PAI14': 3, 'PAI19': 3,
    'PAI7': 3, 'PAI20': 3, 'PAI24': 3,
    # RFQ-18 (max=7, so 8-x)
    'RQF54_2': 7, 'RQF54_7': 7, 'RQF54_14': 7, 'RQF54_27': 7, 'RQF54_38': 7,
    'RQF54_8': 7, 'RQF54_35': 7, 'RQF54_45': 7, 'RQF54_46': 7,
    # SRPS (max=5, so 6-x)
    'SRPS24': 5, 'SRPS22': 5, 'SRPS25': 5, 'SRPS26': 5,
}


# ── Compute subscales from raw data ──────────────────────────────────────────

def compute_subscales(df_raw):
    df = df_raw.copy()

    all_items = set().union(*subscale_items.values())

    for col in all_items:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Apply reverse scoring
    for col, max_val in reverse_specs.items():
        if col in df.columns:
            df[col] = max_val - df[col]

    # Compute subscale means
    subscales = {}
    for scale, items in subscale_items.items():
        available = [i for i in items if i in df.columns]
        missing = [i for i in items if i not in df.columns]
        if missing:
            print(f"WARNING {scale}: missing columns {missing}")
        subscales[scale] = df[available].mean(axis=1)

    df_scales = pd.DataFrame(subscales)
    df_scales = df_scales.rename(columns=rename_dict)
    return df_scales

#%%
# Usage:
df_raw = pd.read_csv('/Users/cweber/Desktop/MPI/MPM/London/AllData_Raw_csv.csv', sep = ',',  encoding='latin-1')
df_raw = df_raw.replace([9999, "9999", "9999.0"], np.nan)
subjects = list(pd.read_csv('/Users/cweber/Desktop/MPI/MPM/London/subjlist.csv')['Subject ID'].values)
relevant_cols = list(pd.read_csv('/Users/cweber/Desktop/MPI/MPM/London/relevant_1.csv')['relevant_1'].values)

df_fsubj = df_raw[df_raw['ID'].isin(subjects)]

df_scales = compute_subscales(df_fsubj)
for col in relevant_cols:
    df_scales[col] = df_fsubj[col]

df_scales.to_csv('/Users/cweber/Desktop/MPI/MPM/London/Data_renamed_forHiTOP.csv')
# %%
