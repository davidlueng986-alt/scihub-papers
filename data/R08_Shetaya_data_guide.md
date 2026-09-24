# Shetaya 2019 Mendeley Data version 1

DOI: https://doi.org/10.17632/xw2kr7ykhd.1. The unchanged publisher dataset ZIP has SHA256 `e04adc7856ef0f607fd92805648725412850d5ef3c522da4a26b15bf4c39af60`, equal to the published file API hash. Keep the original ZIP, and work from its extracted copies.

`DATA FILES/Results/Raw.xlsx` includes six worksheets: instrument-level `Raw` 196Hg readings, `Corrections`, `Processed` with dilution/adsorption formulas, and three additional analysis/graph sheets. `DATA FILES/Results/Processed.xlsx` has soil properties, kinetics and fit worksheets. `DATA FILES/Modelling/` holds soil-specific and collective model workbooks. See `R08_workbook_index.csv` for the 10 workbook and 71 sheet names and declared dimensions. The `Kinetics` sheet declares Excel's maximum row 1,048,576; that is its declared extent, not a verified sample count. Avoid loading that whole sheet into memory by default.

The raw processed worksheet explicitly records a 6 mg/kg 196Hg spike for its observations, 2 g soil and 20 mL solution in initial rows. The proposal's 1 mg/kg spike into SRM 2711a is a different experimental condition. Preserve replicates, raw instrument values, dilution factors, below-quantification entries and model outputs separately. Do not turn 71 sheets or every modeled timepoint into 71 independent observations.
