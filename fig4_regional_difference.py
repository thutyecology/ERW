# -*- coding: utf-8 -*-
"""
Plot cumulative CDR by income group for selected ERW scenarios
(showing only years 2040, 2060, 2080, and 2100).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sces = ['scenario0', 'scenario1', 'scenario2', 'scenario3', 'scenario4']
to_plot = ['scenario0', 'scenario3', 'scenario4']  # example subset

income_group_mapping = {
    '4. Lower middle income': 'Lower middle income',
    '3. Upper middle income': 'Upper middle income',
    '5. Low income': 'Low income',
    '1. High income: OECD': 'High income',
    '2. High income: nonOECD': 'High income'
}
income_order = ['High income', 'Upper middle income', 'Lower middle income', 'Low income']

year_map = {
    'cum_2040': '2040',
    'cum_2060': '2060',
    'cum_2080': '2080',
    'cum_2100': '2100'
}

sns.set(font_scale=2, style="ticks")

for sce in to_plot:
    df = pd.read_csv(f'./data/country_CDR_{sce}.csv')
    df['group'] = df['INCOME_GRP'].replace(income_group_mapping)

    # Keep only selected cumulative years
    keep_cols = ['cum_2040', 'cum_2060', 'cum_2080', 'cum_2100', 'group']
    dfsum = df[keep_cols].groupby('group', as_index=False).sum()

    df_melted = dfsum.melt(
        id_vars='group',
        value_vars=['cum_2040', 'cum_2060', 'cum_2080', 'cum_2100'],
        var_name='Year', value_name='CO2'
    )
    df_melted['Year'] = df_melted['Year'].map(year_map)
    df_melted['CO2'] = df_melted['CO2'] / 1e9  # to GtCO2

    year_order = ['2040', '2060', '2080', '2100']
    df_melted['Year'] = pd.Categorical(df_melted['Year'], categories=year_order, ordered=True)

    fig, ax = plt.subplots(1, 1, figsize=(9, 4), dpi=300)
    sns.barplot(
        data=df_melted,
        x='Year', y='CO2',
        hue='group', hue_order=income_order,
        palette='Oranges_r',
        ci=95, width=0.7, errwidth=1.5, capsize=0.1, ax=ax
    )

    for bar in ax.patches:
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    ax.set_xlabel('')
    if sce == 'scenario0':
        ax.set_ylabel('GtCO2')
        ax.legend(title='', frameon=False, loc='upper left', fontsize=20)
    else:
        ax.set_ylabel('')
        ax.legend_.remove()

    ax.set_ylim(0, 25)
    fig.tight_layout()

    plt.savefig(f'./results/fig4_barplot_CDR_income_{sce}.png', dpi=600, bbox_inches='tight')
    plt.show()
