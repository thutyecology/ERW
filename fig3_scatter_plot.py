# -*- coding: utf-8 -*-
"""
Scatterplots: cropland area vs. cumulative CDR by country,
for three periods under a selected scenario (e.g., Scenario4).
Inputs: ./data/country_CDR_<scenario>.csv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- scenario and data ----
sce = 'scenario4'
df = pd.read_csv(f'./data/country_CDR_{sce}.csv')

# ---- plotting style ----
sns.set(style="ticks", font_scale=1.25)

# ---- regions and colors ----
region_order = [
    "North America",
    "Europe & Central Asia",
    "East Asia & Pacific",
    "Latin America & Caribbean",
    "South Asia",
    "Middle East & North Africa",
    "Sub-Saharan Africa"
]
colors = ['black', 'gray', 'blue', 'fuchsia', 'red', 'darkorange', 'limegreen']
palette = dict(zip(region_order, colors))

# ---- periods and titles ----
periods = ['30_40', '40_50', '50_60']
titles  = ['2030–2040', '2040–2050', '2050–2060']

# ---- figure ----
fig, axs = plt.subplots(3, 1, figsize=(4.5, 11), dpi=300)

for i, period in enumerate(periods):
    # filter and transform
    dfplot = df.copy()
    dfplot = dfplot[dfplot['REGION_WB'].isin(region_order)]
    dfplot = dfplot[(dfplot['cropland_area'] > 0) & (dfplot[period] > 0)]
    dfplot['log_cropland'] = np.log10(dfplot['cropland_area'] * 10000)
    dfplot['log_co2']      = np.log10(dfplot[period] * 10000)

    ax = axs[i]

    # scatter by region
    sns.scatterplot(
        data=dfplot,
        x='log_cropland', y='log_co2',
        hue='REGION_WB', hue_order=region_order, palette=palette,
        edgecolor='black', s=50, alpha=0.85,
        ax=ax, legend=(i == 0)  # legend only on the first panel
    )

    # OLS fit line with 95% CI
    sns.regplot(
        data=dfplot,
        x='log_cropland', y='log_co2',
        scatter=False,
        line_kws={"color": "dodgerblue", "linestyle": "--", "linewidth": 2},
        ci=95, ax=ax
    )

    ax.set_xlabel('log$_{10}$(Cropland area)')
    ax.set_ylabel('log$_{10}$(Cumulative CDR)')
    ax.set_ylim(-1, 11)

# legend on first subplot
axs[0].legend(title='', frameon=False, loc='best', fontsize=9)

plt.tight_layout()

plt.savefig('./results/fig_scatter_plot_country_CDR_cropland.png', dpi=600, bbox_inches='tight')
plt.show()
