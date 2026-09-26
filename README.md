# F1 baseline proposal／SOP：文獻與可用數據

本 repo 保存原有 15 篇 PDF，並加入已核對的表格 CSV、來源清單和用法說明。資料整理日期：2026-09-26。全文、第三方圖表與資料集各有原本的授權及引用條件；此 repo 沒有給它們重新授權。

**此 repo 並非完整 170 MB 資料包。** `full_package_sources_manifest.csv` 和 `full_package_file_manifest.csv` 記錄整份離線資料包的來源與檔案校驗碼；當中的 `papers/`、`datasets/` 等路徑是資料包內的路徑，未必是這個 repo 的路徑。原有 PDF 仍在本 repo 根目錄。未放入 repo 的原始檔可由清單內的官方來源取得；詳細可用狀態見 [UNAVAILABLE.md](UNAVAILABLE.md)。

## 可以直接閱讀和分析

| 內容 | 檔案 | 核心注意事項 |
| --- | --- | --- |
| NIST SRM 2711a 元素及粒度 | [元素 CSV](data/R01_NIST_2711a_element_values.csv)、[粒度 JSON](data/R01_particle_size.json) | NIST 總汞含量不能代替 SOP 的萃取回收率；[證書原文](https://tsapps.nist.gov/srmext/certificates/2711a.pdf)。 |
| R05 Yin et al. 1996 土壤表 1 | [CSV](data/R05_Yin_1996_Table1_soil_characteristics.csv) | 15 種其他土壤；第 4 種的原刊粒度相加是 1020 g/kg，原數照錄並標記。[論文 PDF](R05_Yin_1996_Adsorption_Hg_soil.pdf)。 |
| R06 Yin et al. 1997 表 1–3 | [土壤](data/R06_Yin_1997_Table1_selected_soils.csv)、[動力學擬合](data/R06_Yin_1997_Table2_kinetic_parameters.csv)、[OC 回歸](data/R06_Yin_1997_Table3_OC_regressions.csv) | 表 1／表 2 的土壤編號不同，不能直接按數字合併；擬合參數不是原始時間點。[作者提供論文](https://www1.udel.edu/soilchem/yinest97.pdf)。 |
| R11 Barrow／Cox 1992 | [實驗條件及圖形索引](data/R05_R06_R11_external_data_guide.md) | [原文 PDF](R11_Barrow_Cox_1992_Hg_sorption_II_soil.pdf) 有原圖，但圖 2 仍待附誤差的逐點讀圖；無作者逐點 CSV。 |
| R08 Shetaya et al. 2019 | [資料指南](data/R08_Shetaya_data_guide.md)、[工作表索引](data/R08_workbook_index.csv) | [原版資料集](https://doi.org/10.17632/xw2kr7ykhd.1) 含 10 個 XLSX；實驗條件有別於本 SOP。 |
| **R08 Shetaya 2019：B-version 可機讀數據** | **[B-version dataset folder](data/R08_Shetaya_2019_B/)** | 由與 publisher SHA256 完全一致的 `DATA FILES.zip` 匯出；包括 6 soils × 7 time points 的 clean kinetics、soil properties、instrument/correction/processed exports 及作者模型參數。適合 B 版 adsorption/time calibration；不是 SRM 2711a 的直接實測。 |
| 其他參數 | [熱力學來源表](data/thermodynamic_source_ledger.csv)、[IHSS 方法筆記](data/R21_IHSS_method_note.md) | 核對反應方向、標準態與試驗條件後方可轉用。 |

R08 使用者提供的 `DATA FILES.zip` 已核對 SHA256：
`e04adc7856ef0f607fd92805648725412850d5ef3c522da4a26b15bf4c39af60`，與 `metadata/R08_Mendeley_v1_files.json` 記錄的 Mendeley publisher hash 相同。GitHub 內的 `data/R08_Shetaya_2019_B/` 是為模型與 audit 準備的可機讀 CSV 匯出；publisher ZIP 仍是 archival source of truth。

R05／R06／R11 的頁碼、原單位和方法見 [數據說明](data/R05_R06_R11_external_data_guide.md)。`metadata/` 保留原有 PDF 的核對表、資料集及補充材料來源。

## 原有 PDF 的版本提示

- [R17 Ranz／Marshall](R17_Ranz_Marshall_1952_Evaporation_drops_I_and_II.pdf) 是 **2024 年重新排版的 Part I／II 全文**，不是 1952 年 *Chemical Engineering Progress* 的原刊掃描本。原刊掃描本未找到，毋須當作模型的前置條件。
- [R23 USGS NFM 6.6](R23_USGS_NFM_6.6_Alkalinity_ANC.pdf) 的內頁是 **2012 年 v4.0**，先前 README 寫的 2006 年 v3 不適用於這份 PDF。
- 本 SOP 專屬的 SRM 2711a 汞萃取等實測數據尚未產生；它們不是「文獻無法下載」。
