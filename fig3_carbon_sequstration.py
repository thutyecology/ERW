# -*- coding: utf-8 -*-
"""
Plot global and regional CDR trajectories for ERW scenarios.
Inputs:
  ./data/global_annual_CDR.csv       (columns: Year, Scenario0, Scenario1, Scenario2, Scenario3, Scenario4)
  ./data/global_cumulative_CDR.csv   (columns: Year, Scenario0, Scenario1, Scenario2, Scenario3, Scenario4)
  ./data/regional_CDR.csv            (columns: Year, Region,
                                      Annual_CO2_Mean, Annual_CI_Lower, Annual_CI_Upper,
                                      Cumulative_CO2_Mean, Cumulative_CI_Lower, Cumulative_CI_Upper)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- load data --------------------
dfyear   = pd.read_csv('./data/global_annual_CDR.csv')
dfcum    = pd.read_csv('./data/global_cumulative_CDR.csv')
dfregion = pd.read_csv('./data/regional_CDR.csv')

year = dfyear['Year'].values
zeroes = np.zeros_like(year)   # baseline line (no ERW)

# Scenario labels for legend and titles in panels (a) and (b)
labels = [
    'SSP4 with no ERW',
    'Scenario 0',
    'Scenario 1',
    'Scenario 2',
    'Scenario 3',
    'Scenario 4'
]

# Regions shown in panels (c) and (d)
region_order = [
    "North America",
    "Europe & Central Asia",
    "East Asia & Pacific",
    "Latin America & Caribbean",
    "South Asia",
    "Middle East & North Africa",
    "Sub-Saharan Africa"
]
colors = ['black', 'gray','blue', 'fuchsia','red','darkorange', 'limegreen']



# -------------------- plot style --------------------
sns.set(font_scale=1.9, style="ticks", palette="YlGnBu", color_codes=True)
current_palette = sns.color_palette()

fig, axs = plt.subplots(2, 2, figsize=(18, 13), dpi=300)
x_annot, y_annot = -0.13, 1.06
line_width = 4

# -------------------- (a) Annual global CDR by scenario --------------------
ax = axs[0, 0]
ax.plot(year, zeroes,                lw=line_width, color='k',           label=labels[0])
ax.plot(year, dfyear['Scenario0'],   lw=line_width, color='royalblue',   label=labels[1])
ax.plot(year, dfyear['Scenario1'],   lw=line_width, color=current_palette[5], ls='--', label=labels[2])
ax.plot(year, dfyear['Scenario2'],   lw=line_width, color=current_palette[4], ls='-.', label=labels[3])
ax.plot(year, dfyear['Scenario3'],   lw=line_width+1, color=current_palette[3], ls=':', label=labels[4])
ax.plot(year, dfyear['Scenario4'],   lw=line_width, color='goldenrod', alpha=.8, label=labels[5])
ax.set_title('Annual CO2 sequestered by scenario')
ax.set_xlabel('Year'); ax.set_ylabel('GtCO2')
ax.set_xticks([2030,2040,2050,2060,2070,2080,2090,2100])
ax.text(x_annot, y_annot, 'a', transform=ax.transAxes, fontsize=32, va='top')

# -------------------- (b) Cumulative global CDR by scenario --------------------
ax = axs[0, 1]
ax.plot(year, zeroes,               lw=line_width, color='k',            label=labels[0])
ax.plot(year, dfcum['Scenario0'],   lw=line_width, color='royalblue',    label=labels[1])
ax.plot(year, dfcum['Scenario1'],   lw=line_width, color=current_palette[5], ls='--', label=labels[2])
ax.plot(year, dfcum['Scenario2'],   lw=line_width, color=current_palette[4], ls='-.', label=labels[3])
ax.plot(year, dfcum['Scenario3'],   lw=line_width+1, color=current_palette[3], ls=':', label=labels[4])
ax.plot(year, dfcum['Scenario4'],   lw=line_width, color='goldenrod', alpha=.8, label=labels[5])
ax.set_title('Cumulative CO2 sequestered by scenario')
ax.set_xlabel('Year'); ax.set_ylabel('GtCO2')
ax.set_xticks([2030,2040,2050,2060,2070,2080,2090,2100])
ax.text(x_annot, y_annot, 'b', transform=ax.transAxes, fontsize=32, va='top')
ax.legend(loc='upper left', frameon=False)

# -------------------- (c) Annual regional CDR with 95% CI --------------------
ax = axs[1, 0]
for i, region in enumerate(region_order):
    dfr = dfregion[dfregion['Region'] == region]
    ax.plot(dfr['Year'], dfr['Annual_CO2_Mean'], lw=line_width, color=colors[i], label=region)
    ax.fill_between(dfr['Year'], dfr['Annual_CI_Lower'], dfr['Annual_CI_Upper'], color=colors[i], alpha=0.1)
ax.set_title('Annual CO2 sequestered by region')
ax.set_xlabel('Year'); ax.set_ylabel('GtCO2')
ax.set_xticks([2030,2040,2050,2060,2070,2080,2090,2100])
ax.text(x_annot, y_annot, 'c', transform=ax.transAxes, fontsize=32, va='top')
# ax.legend(loc='upper left', frameon=False)  # uncomment if you want a legend here

# -------------------- (d) Cumulative regional CDR with 95% CI --------------------
ax = axs[1, 1]
for i, region in enumerate(region_order):
    dfr = dfregion[dfregion['Region'] == region]
    ax.plot(dfr['Year'], dfr['Cumulative_CO2_Mean'], lw=line_width, color=colors[i], label=region)
    ax.fill_between(dfr['Year'], dfr['Cumulative_CI_Lower'], dfr['Cumulative_CI_Upper'], color=colors[i], alpha=0.1)
ax.set_title('Cumulative CO2 sequestered by region')
ax.set_xlabel('Year'); ax.set_ylabel('GtCO2')
ax.set_xticks([2030,2040,2050,2060,2070,2080,2090,2100])
ax.text(x_annot, y_annot, 'd', transform=ax.transAxes, fontsize=32, va='top')
ax.legend(loc='upper left', frameon=False)

fig.tight_layout()

plt.savefig('./results/fig3_carbon_sequestration.png', dpi=600, bbox_inches='tight')
plt.show()
