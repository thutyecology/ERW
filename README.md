# Scaling Up Enhanced Rock Weathering for Equitable Climate Change Mitigation

This repository contains the key scripts and data used to reproduce the figures and results presented in the main text of the paper '*Scaling Up Enhanced Rock Weathering for Equitable Climate Change Mitigation*'.  
It includes model outputs and visualization scripts for adoption dynamics, carbon sequestration trajectories, and regional or income-level differences under multiple global ERW deployment scenarios.

---

## 📁 Repository Structure

```
├── data/                        # Input datasets for all figures
│   ├── adoption_shares_<scenario>.csv
│   ├── global_annual_CDR.csv
│   ├── global_cumulative_CDR.csv
│   ├── regional_CDR.csv
│   └── country_CDR_<scenario>.csv
│
├── results/                     # Folder for saving generated figures
│   ├── fig2_adoption_trajectory.png
│   ├── fig3_carbon_sequestration.png
│   ├── fig4_scatter_plot_country_CDR_cropland.png
│   ├── fig5_barplot_CDR_income_<scenario>.png
│
├── fig2_adoption_trajectory.py  # Plot ERW adoption trajectories for five scenarios (0–4)
├── fig3_carbon_sequstration.py  # Plot global and regional CDR trajectories
├── fig4_scatter_plot.py         # Scatterplots of cropland area vs. cumulative CDR
├── fig5_regional_difference.py  # Plot cumulative CDR by income group
└── README.md
```

---

## ⚙️ Environment & Dependencies

All scripts are written in **Python 3.9+** and use standard scientific libraries:

```bash
pip install numpy pandas matplotlib seaborn scipy
```

---

## 📊 Scripts Overview

### `fig2_adoption_trajectory.py`
Plots ERW adoption trajectories for **five scenarios (Scenario 0–4)** using input CSVs with columns:
```
['Year', 'North America', 'Europe & Central Asia', 'East Asia & Pacific',
 'Latin America & Caribbean', 'South Asia', 'Middle East & North Africa', 'Sub-Saharan Africa']
```
**Output:**  
A multi-panel figure showing regional adoption shares (%) over time.

---

### `fig3_carbon_sequstration.py`
Plots **global and regional carbon dioxide removal (CDR)** trajectories under ERW scenarios.

**Inputs:**
- `./data/global_annual_CDR.csv`  
  *(columns: Year, Scenario0–4)*  
- `./data/global_cumulative_CDR.csv`  
  *(columns: Year, Scenario0–4)*  
- `./data/regional_CDR.csv`  
  *(columns: Year, Region, Annual_CO2_Mean, Annual_CI_Lower, Annual_CI_Upper, Cumulative_CO2_Mean, Cumulative_CI_Lower, Cumulative_CI_Upper)*  

**Output:**  
Two global panels (annual & cumulative CDR) and two regional panels with uncertainty shading.

---

### `fig4_scatter_plot.py`
Generates **scatterplots of cropland area vs. cumulative CDR** (log–log scale) for three decadal periods under a selected scenario (e.g., `Scenario4`).

**Input:**  
`./data/country_CDR_<scenario>.csv`  
(columns: `WB_NAME`, `REGION_WB`, `cropland_area`, `30_40`, `40_50`, `50_60`, ...)

**Output:**  
Three vertically stacked scatterplots (2030–2040, 2040–2050, 2050–2060) showing scaling patterns between cropland area and CDR.

---

### `fig5_regional_difference.py`
Plots **cumulative CDR contributions by income group** (High / Upper middle / Lower middle / Low income) for selected scenarios (e.g., Scenario0, Scenario3, Scenario4).

**Input:**  
`./data/country_CDR_<scenario>.csv`

**Output:**  
Bar charts showing total cumulative CDR by income category across selected future years (2040, 2060, 2080, 2100).

---

## 🧭 How to Run

To reproduce the figures:

```bash
python fig2_adoption_trajectory.py
python fig3_carbon_sequstration.py
python fig3_scatter_plot.py
python fig4_regional_difference.py
```

Figures will be displayed interactively and can optionally be saved to `./results/`.

---

## 📬 Contact

For questions or collaborations:  
**Dr. Ying Tu**  
yt668@cornell.edu 

