# Shetaya et al. 2019 data for the B-version Hg(II) model

Source: Shetaya W. (2019), *Data for Sorption kinetics of isotopically labelled divalent mercury (196Hg2+) in soil*, Mendeley Data v1, DOI 10.17632/xw2kr7ykhd.1.

The user-supplied `DATA FILES.zip` was independently verified before extraction. SHA256:

`e04adc7856ef0f607fd92805648725412850d5ef3c522da4a26b15bf4c39af60`

This is identical to the publisher hash recorded in `metadata/R08_Mendeley_v1_files.json`. See `source_manifest.json` for the exact publisher file ID and download URL.

## Files committed for modelling/audit

- `kinetics_clean.csv`: 6 soils × 7 adsorption time points (1, 4, 8, 24, 48, 72, 168 h), extracted from `Results/Processed.xlsx`. This is the main B-version adsorption/time calibration table.
- `soil_properties_clean.csv`: pH, TOC, Al(OH)3, MnO2, Fe2O3 and native Hg for the six soils.
- `raw_instrument.csv`: instrument-level 196Hg export.
- `raw_corrections.csv`: dilution/correction worksheet export.
- `raw_processed.csv`: processed sample-level adsorption observations.
- `raw_final_graphs.csv`: author summary/graph worksheet export.
- `author_model_parameters.csv`: author workbook model parameters.
- `author_model_fit_rsd.csv`: author model fit/RSD comparison.
- `author_elovich_kd_fit.csv`: compact Elovich+Kd parameter/property table.
- `source_manifest.json`: provenance, publisher file ID, URL and SHA256.

## Reproducing the original archive

The connected GitHub writer used here accepts text files but not a local binary ZIP/XLSX stream. Therefore the 15.4 MB publisher ZIP itself is not duplicated in Git history by this import. To materialize the **exact verified archive and XLSX files** inside a clone, run:

```bash
python scripts/download_shetaya_2019.py
```

The script downloads the publisher file, rejects any SHA256 mismatch, writes `data/raw/shetaya_2019/DATA FILES.zip`, and extracts the workbooks.

## Important boundary

The original `Results/Processed.xlsx` has a `Kinetics` worksheet whose declared extent reaches Excel row 1,048,576 because columns Z:AB contain a very large predictive/repeated block. This folder does **not** treat those rows as independent observations. The clean kinetics table uses the experimental summary rows only.

These files are intended to support the B-version model's adsorption/time calibration and audit. They are external-soil data, **not direct SRM 2711a measurements** and do not by themselves validate absolute 2711a extraction percentages.
