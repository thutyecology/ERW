# -*- coding: utf-8 -*-
"""
Plot ERW adoption trajectories for five scenarios (Scenario 0–4)
using input CSV files with columns: ['year', <region names>].
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns

region_labels = [
    "North America",
    "Europe & Central Asia",
    "East Asia & Pacific",
    "Latin America & Caribbean",
    "South Asia",
    "Middle East & North Africa",
    "Sub-Saharan Africa"
]

# Read adoption data for five scenarios (Scenario 0–4)
df0 = pd.read_csv('./data/adoption_shares_scenario0.csv')
df1 = pd.read_csv('./data/adoption_shares_scenario1.csv')
df2 = pd.read_csv('./data/adoption_shares_scenario2.csv')
df3 = pd.read_csv('./data/adoption_shares_scenario3.csv')
df4 = pd.read_csv('./data/adoption_shares_scenario4.csv')

# Extract years and region-level adoption data
year = df0['Year'].values
scenario0 = df0[region_labels].values
scenario1 = df1[region_labels].values
scenario2 = df2[region_labels].values
scenario3 = df3[region_labels].values
scenario4 = df4[region_labels].values
scenarios = [scenario0, scenario1, scenario2, scenario3, scenario4]

# Colors used for regions (consistent across all scenarios)
colors = ['black', 'gray','blue', 'fuchsia','red','darkorange', 'limegreen']

# Labels for each scenario subplot
labels = [
    'Scenario 0 (Baseline)',
    'Scenario 1 (Higher application ceilings)', 
    'Scenario 2 (Earlier kick-offs)',
    'Scenario 3 (More aggressive growth)',
    'Scenario 4 (Human-nature coupled)'
]

# Plot configuration
sns.set(font_scale=1.85, style="ticks", color_codes=True)
fig, axs = plt.subplots(3, 2, figsize=(15, 16), dpi=300)

line_width = 4
ybottom, ytop = -3, 90
alpha = 1
x, y = -0.135, 1.09

# Plot adoption curves for each scenario
for i, ax in enumerate(axs.flat[:-1]):  # use 5 subplots only
    arr = scenarios[i]

    # Add trigger points in Scenario 4
    if i == 4:
        ax.axvline(2037, color="gray", lw=line_width, linestyle=':', alpha=0.5, label="TP1 (2037)")
        ax.axvline(2046, color="gray", lw=line_width, linestyle=':', alpha=0.5, label="TP2 (2046)")
        ax.axvline(2056, color="gray", lw=line_width, linestyle=':', alpha=0.5, label="TP3 (2056)")
        ax.legend()

    # Plot all regions for this scenario
    for j, region in enumerate(region_labels):
        ax.plot(
            year,
            arr[:, j] * 100,       # convert to percentage
            linestyle='-',
            label=region,
            lw=line_width,
            alpha=alpha,
            color=colors[j]
        )

    ax.set_xlabel('Year')
    ax.set_ylabel('ERW adoption share (%)')
    ax.set_ylim(ybottom, ytop)
    ax.set_title(labels[i])
    ax.text(x, y, chr(97 + i), transform=ax.transAxes, fontsize=32, va='top')

# Turn off the last empty subplot
axs[2, 1].axis('off')

fig.tight_layout()

# Create a single legend for all regions
legend_handles = [
    mlines.Line2D([], [], color=colors[j], lw=line_width, alpha=alpha,
                  linestyle='-', label=region_labels[j])
    for j in range(len(region_labels))
]
fig.legend(handles=legend_handles, fontsize=22, loc='lower right', bbox_to_anchor=(0.91, 0.08))

plt.savefig('./results/fig2_adoption_trajectory.png', dpi=600, bbox_inches='tight')
plt.show()
