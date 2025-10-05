import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def bar_charts(df):
    """
    Function to plot bar chart based on the input dataframe
    :param df:  the dataframe
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = plt.cm.viridis(np.linspace(0, 0.8, len(df)))
    bars = ax.bar(df.index, df.values, color=colors, edgecolor="black",
                  linewidth=1, align="center")

    # Create bar in visualization
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:.3f}',
                ha='center', va='bottom', fontsize=9)

    ax.set_label("Important features")
    ax.set_xlabel("Features")
    ax.set_ylabel("Importance Score")