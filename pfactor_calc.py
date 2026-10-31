#%%
import numpy as np
import pandas as pd

pth = '/Users/cweber/Desktop/MPI/MPM/London'

#%%
questionnaire = (
    ["AFI"] * 3
    + ["APSD"] * 3
    + ["BIS-11"] * 3
    + ["BSI"] * 9
    + ["DASI"] * 2
    + ["DERS"] * 6
    + ["DES"] * 3
    + ["ECR-R"] * 2
    + ["EQ"] * 3
    + ["GPTS"] * 2
    + ["IIP-32"] * 8
    + ["LHA"] * 3
    + ["OAS"] * 3
    + ["OPD-SQ"] * 21
    + ["PAI-ANT"] * 3
    + ["PAI-BOR"] * 4
    + ["PCL-C"] * 3
    + ["RFQ-18"] * 2
    + ["SAPAS"] * 1
    + ["SPQ"] * 5
    + ["SRPS"] * 3
)
 
scale = [
    "Authorship", "Interest-taking", "Susceptibility to control",
    "Callousness", "Impulsiveness", "Narcissism",
    "Attentional impulsiveness", "Motor impulsiveness", "Non-planning impulsiveness",
    "Anxiety", "Depression", "Hostility", "Interpersonal sensitivity",
    "Obsessive-compulsive", "Paranoid ideation", "Phobia", "Psychoticism", "Somatoform",
    "Drugs and alcohol", "Self-harm",
    "Emotion-regulation strategies", "Emotional awareness", "Emotional clarity",
    "Goal-directed behavior", "Impulse control", "Nonacceptance of emotions",
    "Absorption", "Amnestic dissociation", "Depersonalization",
    "Attachment anxiety", "Attachment avoidance",
    "Cognitive empathy", "Emotional reactivity", "Social skills",
    "Feelings of persecution", "Thoughts of social referencing",
    "Cold", "Domineering", "Intrusive", "Nonassertive", "Overly accommodating",
    "Self-sacrificing", "Socially inhibited", "Vindictive",
    "Aggression", "Antisocial behavior", "Self-directed aggression",
    "Feelings of emptiness", "Feelings of inferiority", "Reactions of others",
    "Accepting help", "Affect differentiation", "Affect tolerance", "Anticipation",
    "Balancing interests", "Communicating affect", "Detaching relationships",
    "Empathy", "Establishing contact", "Experiencing affect",
    "Holistic object perception", "Impulse Control", "Internalization",
    "Perceiving bodily self", "Realistic object perception",
    "Regulation of self-esteem", "Self-object differentiation", "Self-perception",
    "Sense of identity", "Use of introjects", "Use of phantasy",
    "Antisociality", "Egocentricity", "Sensation-seeking",
    "Affective instability", "Identity problems", "Negative relationships", "Self-harm",
    "Avoidance", "Hyperarousal", "Re-experiencing",
    "Mentalizing of others", "Mentalizing of self",
    "Personality pathology",
    "Mistrust", "Oddity", "Social anhedonia", "Social anxiety", "Unusual beliefs",
    "Antisociality", "Callousness", "Egocentricity",
]
 
P = [
    0.46, -0.18, 0.60,
    0.25, 0.78, 0.46,
    0.82, 0.71, 0.61,
    0.80, 0.81, 0.77, 0.85, 0.84, 0.84, 0.77, 0.90, 0.76,
    0.25, 0.65,
    0.84, 0.40, 0.78, 0.73, 0.79, 0.75,
    0.74, 0.58, 0.71,
    0.73, 0.50,
    0.15, 0.22, 0.75,
    0.65, 0.80,
    0.68, 0.70, 0.44, 0.52, 0.63, 0.57, 0.62, 0.48,
    0.56, 0.45, 0.79,
    0.75, 0.73, 0.80,
    0.55, 0.83, 0.84, 0.81, 0.74, 0.83, 0.66, 0.49, 0.68, 0.74, 0.70, 0.78, 0.84, 0.83, 0.65,
    0.79, 0.82, 0.83, 0.83, 0.77, -0.14,
    0.57, 0.52, 0.59,
    0.84, 0.86, 0.81, 0.76,
    0.80, 0.83, 0.71,
    0.44, 0.85,
    0.84,
    0.80, 0.73, 0.82, 0.70, 0.57,
    0.86, 0.19, 0.44,
]
 
INT = [
    -0.04, -0.15, 0.29,
    -0.14, -0.07, 0.00,
    0.18, -0.16, -0.08,
    0.34, 0.35, 0.13, 0.21, 0.24, 0.16, 0.24, 0.31, 0.16,
    -0.08, 0.25,
    0.32, 0.00, 0.14, 0.24, 0.26, 0.25,
    0.02, -0.14, 0.00,
    0.14, 0.00,
    0.05, -0.37, 0.10,
    0.06, -0.01,
    0.02, -0.07, 0.11, 0.15, 0.16, 0.22, 0.21, 0.01,
    -0.05, -0.14, 0.22,
    0.25, 0.33, 0.16,
    0.21, 0.37, 0.40, 0.23, 0.09, 0.24, 0.45, 0.32, 0.20, 0.20, 0.26, 0.17, 0.16, 0.23, 0.24,
    0.40, 0.30, 0.31, 0.42, 0.31, 0.18,
    -0.25, -0.24, -0.28,
    0.22, 0.37, 0.19, -0.03,
    0.26, 0.29, 0.31,
    0.15, 0.19,
    0.17,
    0.18, -0.03, -0.07, 0.15, -0.12,
    0.07, -0.05, -0.28,
]
 
THO = [
    -0.14, -0.03, -0.01,
    0.00, -0.03, -0.06,
    0.03, -0.04, -0.02,
    0.10, -0.04, 0.06, -0.05, 0.05, 0.15, 0.18, 0.02, 0.15,
    0.04, 0.00,
    -0.13, -0.16, -0.10, -0.17, -0.01, -0.13,
    0.42, 0.44, 0.48,
    -0.09, -0.02,
    0.01, -0.09, -0.02,
    0.32, 0.17,
    0.02, -0.08, 0.10, -0.03, -0.02, 0.09, 0.01, 0.03,
    0.06, 0.20, 0.04,
    0.10, 0.05, 0.06,
    -0.10, 0.00, 0.02, 0.11, -0.05, 0.04, 0.05, 0.12, -0.10, 0.00, 0.09, -0.06, 0.06, 0.05, 0.17,
    -0.13, 0.19, -0.04, 0.07, -0.13, -0.11,
    0.12, -0.02, 0.04,
    -0.10, -0.07, 0.02, -0.03,
    -0.05, 0.00, 0.04,
    0.06, -0.07,
    -0.01,
    0.19, 0.19, 0.02, -0.02, 0.36,
    -0.03, -0.01, 0.01,
]
 
DET = [
    0.13, 0.17, -0.03,
    0.20, -0.03, -0.12,
    0.05, -0.08, 0.08,
    -0.11, -0.03, -0.18, -0.06, -0.06, -0.06, 0.05, -0.03, -0.14,
    -0.16, -0.05,
    -0.05, 0.17, 0.07, -0.09, -0.04, -0.04,
    -0.03, 0.05, 0.03,
    -0.01, 0.47,
    0.35, 0.23, 0.43,
    -0.07, -0.08,
    0.42, -0.16, -0.28, 0.22, 0.11, -0.03, 0.36, 0.17,
    -0.14, -0.03, -0.02,
    0.09, 0.13, 0.02,
    0.38, 0.10, -0.05, 0.10, -0.05, 0.18, -0.09, -0.05, 0.39, 0.25, 0.12, -0.09, 0.18, 0.13, 0.06,
    0.16, 0.21, 0.14, 0.08, 0.14, 0.08,
    -0.07, -0.05, -0.13,
    -0.04, -0.04, -0.04, -0.01,
    0.01, -0.09, -0.19,
    0.34, 0.04,
    0.19,
    0.06, 0.10, 0.38, 0.28, -0.19,
    -0.01, 0.07, -0.01,
]
 
ANT = [
    0.01, 0.15, -0.05,
    0.75, 0.09, 0.69,
    -0.01, -0.08, -0.01,
    -0.04, -0.04, 0.23, -0.15, -0.06, 0.07, -0.02, -0.01, -0.09,
    -0.04, -0.11,
    -0.07, -0.04, -0.09, -0.06, 0.04, -0.11,
    -0.01, -0.06, -0.02,
    -0.04, -0.05,
    0.24, 0.64, 0.04,
    0.07, -0.04,
    0.09, 0.39, 0.08, -0.29, -0.33, -0.32, -0.03, 0.33,
    0.15, 0.21, -0.09,
    0.04, 0.00, 0.00,
    0.02, 0.06, -0.01, 0.15, 0.26, 0.23, -0.02, -0.29, -0.09, 0.09, 0.32, 0.10, 0.15, -0.03, 0.02,
    -0.07, 0.07, -0.04, 0.05, -0.07, 0.00,
    0.28, 0.54, 0.08,
    -0.03, -0.03, 0.05, 0.00,
    0.01, 0.01, -0.03,
    0.20, 0.07,
    0.08,
    0.07, 0.00, 0.12, -0.07, -0.07,
    0.24, 0.56, 0.53,
]
 
DIS = [
    0.25, 0.11, -0.09,
    0.15, 0.59, -0.05,
    0.24, 0.51, 0.60,
    -0.14, -0.09, 0.00, -0.11, -0.06, -0.09, -0.07, -0.10, -0.15,
    0.30, 0.11,
    0.08, 0.04, 0.06, 0.08, 0.31, -0.02,
    0.05, 0.06, -0.06,
    0.08, 0.08,
    0.15, -0.03, 0.00,
    -0.07, -0.13,
    -0.03, 0.07, 0.07, -0.01, -0.01, 0.08, -0.08, -0.06,
    0.22, 0.36, 0.15,
    0.05, -0.01, -0.07,
    0.03, 0.09, 0.09, 0.20, 0.25, 0.13, 0.13, 0.14, -0.02, 0.10, 0.15, 0.27, -0.01, -0.01, 0.20,
    0.08, 0.09, 0.06, 0.10, 0.11, 0.02,
    0.37, 0.16, 0.32,
    0.18, 0.09, 0.15, 0.55,
    -0.06, 0.03, -0.07,
    0.14, 0.17,
    0.17,
    0.03, 0.07, -0.10, -0.05, -0.02,
    0.29, 0.11, -0.03,
]
 
_N_EXPECTED = 92
_lengths = {
    "questionnaire": len(questionnaire), "scale": len(scale), "P": len(P),
    "INT": len(INT), "THO": len(THO), "DET": len(DET), "ANT": len(ANT), "DIS": len(DIS),
}
_bad = {k: v for k, v in _lengths.items() if v != _N_EXPECTED}
if _bad:
    raise ValueError(f"Coefficient vectors do not all have length {_N_EXPECTED}: {_bad}")
 
coef_table = pd.DataFrame({
    "questionnaire": questionnaire,
    "scale": scale,
    "P": P,
    "INT": INT,
    "THO": THO,
    "DET": DET,
    "ANT": ANT,
    "DIS": DIS,
})

coef_table["label"] = coef_table["questionnaire"] + " " + coef_table["scale"]
 
del questionnaire, scale, P, INT, THO, DET, ANT, DIS, _lengths, _bad, _N_EXPECTED
 

# POMP scaling

QUESTIONNAIRE_RANGE = {
    "AFI":     (1, 5),
    "APSD":    (0, 2),
    "BIS-11":  (1, 4),
    "BSI":     (0, 4),
    "DASI":    (0, 4),
    "DERS":    (1, 5),
    "DES":     (0, 100),
    "ECR-R":   (1, 6),
    "EQ":      (0, 3),
    "GPTS":    (1, 5),
    "IIP-32":  (0, 4),
    "LHA":     (0, 5),
    "OAS":     (0, 4),
    "OPD-SQ":  (0, 4),
    "PAI-ANT": (0, 3),
    "PAI-BOR": (0, 3),
    "PCL-C":   (1, 5),
    "RFQ-18":  (1, 7),
    "SAPAS":   (0, 1),
    "SPQ":     (0, 1),
    "SRPS":    (1, 5),
}
 

pomp_ranges = {
    row.label: QUESTIONNAIRE_RANGE[row.questionnaire]
    for row in coef_table.itertuples()
}
 
DEFAULT_SCALES_INVERT = [
    "AFI Authorship", "AFI Interest-taking", "AFI Susceptibility to control",
    "EQ Cognitive empathy", "EQ Emotional reactivity", "EQ Social skills",
]
 
 
def pomp(series, lo, hi):
    """Percent-of-maximum-possible transform: rescale to a fixed 0-100
    metric using the scale's known theoretical response range."""
    return (series - lo) / (hi - lo) * 100
 
 
def pomp_score_scales(df, scales, ranges=None, invert=None):
    """
    POMP-transform (0-100) each requested raw scale score using its known
    response range, then invert scales 
    """
    ranges = pomp_ranges if ranges is None else ranges
    invert = DEFAULT_SCALES_INVERT if invert is None else invert
 
    df_pomp = pd.DataFrame(index=df.index)
    for col in scales:
        lo, hi = ranges[col]
        df_pomp[col] = pomp(df[col], lo, hi)
 
    for col in invert:
        if col in df_pomp.columns:
            df_pomp[col] = 100 - df_pomp[col]
 
    return df_pomp

 
def list_available_scales(pattern=None):
    labels = coef_table["label"]
    if pattern is not None:
        labels = labels[labels.str.contains(pattern, case=False, regex=True)]
    return labels.tolist()
 
 
def classify_scales(threshold = 0.20):
    spectra = ["INT", "THO", "DET", "ANT", "DIS"]
    classifications = []
    for _, row in coef_table.iterrows():
        marked = [s for s in spectra if abs(row[s]) >= threshold]
        p_marked = abs(row["P"]) >= threshold
        if len(marked) == 0 and p_marked:
            cls = "Pure marker of P"
        elif len(marked) == 1:
            cls = f"Pure marker of {marked[0]}"
        elif len(marked) > 1:
            cls = "Blend of " + " + ".join(marked)
        else:
            cls = "Not captured by HiTOP"
        classifications.append(cls)
    return pd.DataFrame({"label": coef_table["label"], "classification": classifications})
 
 
def compute_hitop_scores(df_pomp, factors=("P",), min_loading=0.0, na_rm=True,
                          standardize_method="zscore", norms=None):
    """
    Compute weighted-composite HiTOP scores (P/spectra)
    """
    coef_lookup = coef_table.set_index("label")
    available = [c for c in df_pomp.columns if c in coef_lookup.index]
    if not available:
        raise ValueError("None of df_pomp's columns match coef_table['label']. "
                          "Use list_available_scales() to check valid labels.")
 
    if standardize_method == "zscore":
        z = df_pomp[available].apply(lambda x: (x - x.mean()) / x.std(ddof=1))
    elif standardize_method == "none":
        z = df_pomp[available].copy()
    elif standardize_method == "fixed":
        if norms is None:
            raise ValueError("norms= must be supplied when standardize_method='fixed'.")
        missing_norms = [c for c in available if c not in norms]
        if missing_norms:
            raise ValueError(f"Missing norms for: {missing_norms}")
        z = pd.DataFrame({c: (df_pomp[c] - norms[c][0]) / norms[c][1] for c in available},
                          index=df_pomp.index)
    else:
        raise ValueError("standardize_method must be 'zscore', 'none', or 'fixed'.")
 
    out = pd.DataFrame(index=df_pomp.index)
 
    for f in factors:
        w = coef_lookup.loc[available, f]
 
        if min_loading > 0:
            keep = w.abs() >= min_loading
            w = w[keep]
            zz = z[w.index]
        else:
            zz = z[available]
 
        if len(w) == 0 or w.isna().all():
            print(f"Warning: no scales with sufficient loading on {f}; returning NaN.")
            out[f] = np.nan
            continue
 
        if na_rm:
            def _row_score(row, w=w):
                ok = row.notna()
                if not ok.any():
                    return np.nan
                return float((row[ok] * w[ok]).sum() / w[ok].abs().sum())
            out[f] = zz.apply(_row_score, axis=1)
        else:
            out[f] = zz.values.dot(w.values) / np.abs(w.values).sum()
 
    return out
 

if __name__ == "__main__":
 
    pth = "."  

    df_hitop_all = pd.read_csv(f"{pth}/Data_renamed_forHiTOP.csv", sep=",", encoding="latin-1")
    df_hitop = df_hitop_all[df_hitop_all["Gender"] != 3].copy()
 
    # which scales does this dataset actually have? 
    scales_invert = [c for c in DEFAULT_SCALES_INVERT if c in df_hitop.columns]
    scales_keep = [c for c in coef_table["label"]
                   if c in df_hitop.columns and c not in scales_invert]
    all_scales = scales_keep + scales_invert
    print(f"Found {len(all_scales)}/{len(coef_table)} established scales in this dataset.")
 
    # POMP, invert
    df_pomp = pomp_score_scales(df_hitop, all_scales, invert=scales_invert)
 
    coef_lookup = coef_table.set_index("label")
    retained = [c for c in all_scales if abs(coef_lookup.loc[c, "P"]) >= 0.40]
    print(f"Retained {len(retained)}/{len(all_scales)} scales as strong P markers (|loading| >= .40)")
 
    # compute factors
    scores = compute_hitop_scores(
        df_pomp,
        factors=["P", "INT", "THO", "DET", "ANT", "DIS"],
        standardize_method="zscore",  
    )
    p_factor = scores["P"].to_numpy()  

    df_new = df_hitop.copy()
    df_new["p_HiTOP"] = p_factor
    for spec in ["INT", "THO", "DET", "ANT", "DIS"]:
        df_new[f"{spec}_HiTOP"] = scores[spec]

    df_recoding = pd.read_csv(f'{pth}/coding.csv')
    recoding = dict(zip(df_recoding['Subject_ID'].values, df_recoding['consecutive'].values))

    df_new['ID'] = df_new['ID'].replace(recoding).copy()
 
    df_new.to_csv(f"{pth}/clindata_withp_HiTOP.csv", index=False)
 
    import seaborn as sbn
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 6, figsize=(20, 2), sharey = True)
    colors = {1:"#7265a6",2: "#f4cb00", 4: "#28a9a2", 3 :"#697272"}
        
    for f, factor in enumerate(["ANT", "INT", "THO", "DET", "DIS", "p"]):
        sbn.kdeplot(df_new, x=f"{factor}_HiTOP", hue="Referral_Diagnosis",  palette = colors, multiple = 'stack', fill = False, legend = False, ax= ax[f])
        sbn.histplot(df_new, x=f"{factor}_HiTOP", hue="Referral_Diagnosis", multiple = 'stack', palette = colors, alpha = 0.6, stat = 'density', legend = False, ax = ax[f])
        ax[f].set_ylabel(factor)
    fig.savefig('p_factor_distribution_h.png', bbox_inches = 'tight')

    # sanity check
    print(classify_scales().set_index("label").loc[all_scales])
# %%
df_new[["p_HiTOP", "Referral_Diagnosis"]]
# %%
