# Shetaya et al. 2019 data for the B-version Hg(II) model

Source: Shetaya W. (2019), *Data for Sorption kinetics of isotopically labelled divalent mercury (196Hg2+) in soil*, Mendeley Data v1, DOI 10.17632/xw2kr7ykhd.1.

The user-supplied `DATA FILES.zip` was verified before extraction. SHA256: `e04adc7856ef0f607fd92805648725412850d5ef3c522da4a26b15bf4c39af60`. This is identical to the publisher hash already recorded in `metadata/R08_Mendeley_v1_files.json`.

## Files

- `kinetics_clean.csv`: the 6-soil × 7-time-point adsorption summary (1, 4, 8, 24, 48, 72, 168 h) from `Results/Processed.xlsx`, suitable for B-version adsorption/time calibration.
- `soil_properties_clean.csv`: pH, TOC, Al(OH)3, MnO2, Fe2O3 and native Hg for the six soils.
- `raw_instrument.csv`, `raw_corrections.csv`, `raw_processed.csv`, `raw_final_graphs.csv`: GitHub-friendly exports of the source `Results/Raw.xlsx` worksheets.
- `author_model_parameters.csv`, `author_model_fit_rsd.csv`, `author_elovich_kd_fit.csv`: author workbook model outputs retained for comparison; these are not automatically adopted as SRM 2711a parameters.

## Important boundary

The original `Results/Processed.xlsx` has a `Kinetics` worksheet whose declared extent reaches Excel row 1,048,576 because columns Z:AB contain a very large predictive/repeated block. This folder does **not** treat those rows as independent observations. The clean kinetics table uses the experimental summary rows 4–45 only.

These files are derived CSV exports for modelling and audit. The publisher ZIP remains the archival source of truth.
