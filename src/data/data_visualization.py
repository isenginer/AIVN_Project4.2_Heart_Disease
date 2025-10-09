import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif


def bar_charts(series, k=10):
    """
    Function to plot bar chart based on the input dataframe
    :param df:  the dataframe
    """
    df = series.iloc[:k]
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = plt.cm.viridis(np.linspace(0, 1.2, len(df)))
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


def mutual_barhs(X_train, y_train):
    """
    Function to plot bar chart based on the input to get the mutual information
    MI function to find the best relative mutual information
    :param X_train: Train data frame
    :param y_train: Train label series
    :return: the mutual information barh
    """
    pass